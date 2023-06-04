import requests
from _datetime import datetime
#
# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# response.raise_for_status()
# longitude = response.json()["iss_position"]["longitude"]
# latitude = response.json()["iss_position"]["latitude"]
# data = (longitude, latitude)
# print(data)
MY_LONG = 36.821945
MY_LAT = -1.292066
parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0
}
time_now = datetime.now()
response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data['results']['sunrise'].split("T")[1].split(':')[0]
sunset = data['results']['sunset'].split("T")[1].split(':')[0]
print(sunrise)  # in 12 hr format
print(sunset)  # in 12 hr format
print(time_now.hour)
