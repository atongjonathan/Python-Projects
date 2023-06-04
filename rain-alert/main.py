
from twilio.rest import Client
import os

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
