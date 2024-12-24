import requests
from datetime import datetime, timedelta
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_API_KEY = "FYRCRQHV42TOTGLA"
STOCK_URL = f"https://www.alphavantage.co/query"

ACCOUNT_SID = "ACb74f1548e9b8f0cf752277336ddb9857"
PHONE = "+15855952560"
AUTH_TOKEN = "75eebcfa9f2677bfc25ba6d8c1dce877"

NEWS_API_KEY = "6e7bc025ee284856af75ce00a53eef6c"
NEWS_URL = "https://newsapi.org/v2/everything"

today = datetime.now().date()
today.strftime("%Y-%m-%d")
yesterday = today
day_before_yesterday = today
if datetime.now().weekday() == 6:
    yesterday = today - timedelta(days=2)
    day_before_yesterday = yesterday - timedelta(days=1)
elif datetime.now().weekday() == 0:
    yesterday = today - timedelta(days=3)
    day_before_yesterday = yesterday - timedelta(days=1)
elif datetime.now().weekday() == 1:
    yesterday = today - timedelta(days=1)
    day_before_yesterday = yesterday - timedelta(days=4)
day_before_yesterday = str(day_before_yesterday.strftime("%Y-%m-%d"))
yesterday = str(yesterday.strftime("%Y-%m-%d"))
today = str(today.strftime("%Y-%m-%d"))


parameter_news = {
    "apiKey": NEWS_API_KEY,
    "qInTitle": COMPANY_NAME,
    "language": 'en'
}

parameters_stock = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": STOCK_API_KEY,
}

news_response = requests.get(url=NEWS_URL, params=parameter_news)
stock_response = requests.get(url=STOCK_URL, params=parameters_stock)
stock_data = stock_response.json()
news_data = news_response.json()["articles"]


def is_change():
    percentage_change = ((float(stock_data["Time Series (Daily)"][yesterday]["1. open"]) - float(
        stock_data["Time Series (Daily)"][day_before_yesterday][
            "4. close"])) / (float(stock_data["Time Series (Daily)"][yesterday]["1. open"]))) * 100
    return abs(percentage_change)


arrow = None
if is_change() > 0:
    up_down = "🔺"
else:
    up_down = "🔻"

formatted_articles = [f"{STOCK}: {up_down}{is_change()}%\nHeadline: {article['title']}. \nBrief: {article['description']}" for article in news_data]
client = Client(ACCOUNT_SID, AUTH_TOKEN)
message = client.messages.create(
   body=formatted_articles,
   from_=PHONE,
   to="+919479702980"
   )
