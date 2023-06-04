# import requests
from twilio.rest import Client
import os

account_sid = "AC02d3f350641fa7e70a80d2e9e599377b"
auth_token = "c485520cea0a52a66ddc2b5959ff4948"
OWM_endpoint = "https://api.openweathermap.org/data/2.5/weather"
api_key = "8d10ebe81248b8386d7dc8b5b019d6f5"
# parameters = {
#     "lat": -1.292066,
#     "lon": 36.821945,
#     "appid": api_key,
# }
# response = requests.get(url=OWM_endpoint, params=parameters)
# response.raise_for_status()
# data = response.json()
# print(data)
client = Client(account_sid, auth_token)
message = client.messages \
                .create(
                     body="Join Earth's mightiest heroes. Like Kevin Bacon.",
                     from_='+13613104160',
                     to='+254708683896'
                 )
print(message.status)
