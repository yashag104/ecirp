import requests
from twilio.rest import Client
import random
import os

API_KEY = "b01bbcd6885a746b5ddfdbabfa2f864b"
ACCOUNT_SID = "AC339409e944224d1ef4b17cb2e6315672"
PHONE = "+17194276458"
WHATSAPP = "+14155238886"
AUTH_TOKEN = "5012b820c4061aab8e733f07ba60933d"
# LANGUAGE = "en"
# Locations = {
#     "damoh": {
#         "lat": 23.838099,
#         "lng": 79.442169
#     },
#     "pilani": {
#         "lat": 28.363800,
#         "lng": 75.600998
#     },
#     "indore": {
#         "lat": 22.719568,
#         "lng": 75.857727
#     }
#
# }
#
# parameters = {
#     "appid": API_KEY,
#     "units": "metric",
#     "lon": Locations["damoh"]["lng"],
#     "lat": Locations["damoh"]["lat"],
#     "cnt": 4,
#     "lang": LANGUAGE
# }
#
# response = requests.get(url=f"https://api.openweathermap.org/data/2.5/forecast", params=parameters)
# weather = response.json()
# for entry in weather['list']:
#     if entry["weather"][0]["id"] < 700:
#         print("bring an umbrella")
#sid = os.environ["TWILIO_ACCOUNT_SID"]
#auth = os.environ["TWILIO_AUTH_TOKEN"]
with open("quotes.txt") as quote_file:
    all_quotes = quote_file.readlines()
    quote = random.choice(all_quotes)
client = Client(ACCOUNT_SID, AUTH_TOKEN)
message = client.messages.create(
    body="Hi, I am learning python.",
    from_=PHONE,
    to="+919479702980"
)
