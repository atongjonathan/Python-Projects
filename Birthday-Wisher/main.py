import datetime as dt
import smtplib
import pandas as pd
import random

my_email = "atongjonathan5@gmail.com"
password = "opszsbdfvvscagvr"
send_to = ""

today = dt.datetime.now()
day = today.day
month = today.month
year = today.year

data = pd.read_csv("birthdays.csv")
birth_day = data.year
birth_month = data.year
birth_year = data.year
name = ''


def is_it_today():
    for (index, row) in data.iterrows():
        if row.day == day and row.month == month and row.year == year:
            global name
            name = data.name[index]
            global send_to
            send_to = row.email
            return True
        else:
            return False

is_it_today()
chosen_letter = f"../Birthday-Wisher/letters/letter_{random.randint(1, 3)}.txt"
with open(chosen_letter) as file:
    letter = file.read()
letter = letter.replace("[NAME]", name).replace("Angela", "- Jona")
# Sending the letter
try:
    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()  # Make connection Secure
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=send_to,
                            msg=f"Subject:Happy Birthday!\n\n{letter}")
    print("Letter Sent")
except UnicodeError :
    print("Letter Not Sent")
