import requests
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

account_sid = "AC02d3f350641fa7e70a80d2e9e599377b"
auth_token = "c485520cea0a52a66ddc2b5959ff4948"

parameters = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK_NAME,
    "apikey": "3CIL17SKE7USP3RL",
}

stock_response = requests.get(url=STOCK_ENDPOINT, params=parameters)
stock_response.raise_for_status()
stock_data = stock_response.json()

days_stocks = stock_data["Time Series (Daily)"]
closes = [value["4. close"] for (key, value) in days_stocks.items()]
days = [key for (key, value) in days_stocks.items()]
yesterday_close = float(closes[0])
day_before_close = float(closes[1])
difference = yesterday_close - day_before_close

news_url = "https://newsapi.org/v2/everything"
news_params = {
    "apiKey": "6bead539ec66436ca864d9aaef76ae7d",
    "q": COMPANY_NAME,
    "from": days[0],
    "to": days[1],
}
news_response = requests.get(url=news_url, params=news_params)
news_response.raise_for_status()
news = news_response.json()
first_3_articles = news["articles"][:3]

articles = [f"Headline:\n {item['title']} \nBrief:\n {item['description']}" for item in first_3_articles]
message = '\n'.join(articles)
percentage = abs(difference) * 100
print(difference, "\n", percentage)

if difference >= 0:
    up_down = "🔺"
else:
    up_down = "🔻"

client = Client(account_sid, auth_token)
if percentage > 5:
    message = client.messages \
        .create(body=f"TSLA: {up_down}{percentage}%\n{message}", from_='+13613104160', to='+254708683896')
    print("Sent")
