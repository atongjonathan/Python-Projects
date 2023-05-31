import smtplib
import datetime as dt
import random

with open("quotes.txt") as file:
    quotes = file.readlines()
todays_quote = random.choice(quotes)
now = dt.datetime.now()
year = now.year
day_of_week = now.weekday()
if day_of_week == 0:
    my_email = 'atongjonathan5@gmail.com'
    password = 'opszsbdfvvscagvr'

    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()  # Secure connection
        connection.login(user=my_email, password=password)
        try:
            connection.sendmail(from_addr=my_email,
                                to_addrs="atongjonathan@gmail.com",
                                msg=f"Subject:Motivation\n\n{random.choice(quotes)}")
            print("Sent")
        except UnicodeError:
            print("Not Sent")





