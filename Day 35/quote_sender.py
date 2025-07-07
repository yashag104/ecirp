import random

from twilio.rest import Client

ACCOUNT_SID = "ACb74f1548e9b8f0cf752277336ddb9857"
PHONE = "+15855952560"
AUTH_TOKEN = "75eebcfa9f2677bfc25ba6d8c1dce877"

with open("quotes.txt") as file:
    quotes = file.readlines()
    quotes = [quote.strip() for quote in quotes]
    quote = random.choice(quotes)
    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    message = client.messages.create(
        body=f"Good Morning!!\n{quote}\nHave a good day",
        from_=PHONE,
        to="+919479702980"
    )
