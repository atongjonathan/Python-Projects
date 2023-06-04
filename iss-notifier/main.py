import requests
from datetime import datetime
import smtplib
import time

MY_LAT = -1.292066
MY_LONG = 36.821945
my_email = "atongjonathan5@gmail.com"
my_password = "opszsbdfvvscagvr"


def iss_is_near():
    response_iss = requests.get(url="http://api.open-notify.org/iss-now.json")
    response_iss.raise_for_status()
    data = response_iss.json()
    iss_longitude = float(data["iss_position"]["longitude"])
    iss_latitude = float(data["iss_position"]["latitude"])
    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5:
        return True
    else:
        return False


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }
    response_sunset = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    response_sunset.raise_for_status()
    data_sun = response_sunset.json()
    sunrise = int(data_sun["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data_sun["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour
    if time_now >= sunset or time_now <= sunrise:
        return True


while time.sleep(60):
    if iss_is_near() and is_night():
        with smtplib.SMTP('smtp.gmail.com') as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_password)
            connection.sendmail(from_addr=my_email,
                                to_addrs="atongjonathan@gmail.com",
                                msg="Subject: Look Up👆\n\nThe ISS is above you in the sky!")
