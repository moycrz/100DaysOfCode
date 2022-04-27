import requests
from twilio.rest import Client
from datetime import *
from bs4 import BeautifulSoup
import os

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
body_message = ""

# TODO: STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
if datetime.now().month < 10:
    today = f"{datetime.now().year}-0{datetime.now().month}-{datetime.now().day}"
    yesterday = f"{datetime.now().year}-0{datetime.now().month}-{datetime.now().day - 1}"
else:
    today = f"{datetime.now().year}-{datetime.now().month}-{datetime.now().day}"
    yesterday = f"{datetime.now().year}-{datetime.now().month}-{datetime.now().day - 1}"

API_KEY = os.environ.get("AUTH_TOKEN_ALPHA")
API_Endpoint = "https://www.alphavantage.co/query"
parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": API_KEY,
}

response = requests.get(API_Endpoint, params=parameters)
response.raise_for_status()
data_daily = response.json()["Time Series (Daily)"]
data_daily_open = float(data_daily[today]["1. open"])
data_daily_close = float(data_daily[today]["4. close"])

# TODO: STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
API_KEY_NEWSAPI = os.environ.get("AUTH_TOKEN_NEWSAPI")
API_Endpoint = "https://newsapi.org/v2/everything"
parameters = {
    "q": COMPANY_NAME,
    "from": yesterday,
    "to": today,
    "sortBy": "popularity",
    "apiKey": API_KEY_NEWSAPI,
}

response = requests.get(API_Endpoint, params=parameters)
response.raise_for_status()
data = response.json()["articles"][0]
title = data["title"]
resume = BeautifulSoup(data["description"], features="html.parser")
resume = resume.get_text()

# TODO: STEP 3: Use https://www.twilio.com
# Send a separate message with the percentage change and each article's title and description to your phone number.
account_sid = 'ACee986c7e770dfb8039d211122c541951'
auth_token = os.environ.get("AUTH_TOKEN")

if data_daily_open > data_daily_close:
    percentage = round(100 - (data_daily_close/data_daily_open * 100), 2)
    body_message = f"TSLA: [DOWN] {percentage}%" \
                   f"Headline: {title}" \
                   f"Brief: {resume}"
else:
    percentage = round((data_daily_close/data_daily_open * 100)-100, 2)
    body_message = f"""
        {STOCK}: [UP] {percentage}%, 
        Headline: {title}, 
        Brief: {resume}
    """

client = Client(account_sid, auth_token)
message = client.messages.create(
    body=body_message,
    from_='+19206858193',
    to='+527717051973'
)
print(message.status)

# Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file
 by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the 
 coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file
 by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the 
 coronavirus market crash.
"""
