import requests
from twilio.rest import Client
import os

account_sid = 'ACee986c7e770dfb8039d211122c541951'
auth_token = os.environ.get("AUTH_TOKEN")

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
API_KEY = os.environ.get("OWM_API_KEY")
parameters = {
    "lat": 19.975370,
    "lon": -99.173500,
    "appid": API_KEY,
    "exclude": "current,minutely,hourly",
}

response = requests.get(OWM_Endpoint, params=parameters)
response.raise_for_status()
data = response.json()["daily"]
weather_data = [weather["weather"] for weather in data]
weather_id = [weather_data[i][0]["id"] for i in range(0, len(data) - 1)]
will_rain = False

for w_id in weather_id:
    if w_id < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body="It's going to rain today. Remember to bring an ☔.",
        from_='+19206858193',
        to='+527717051973'
    )
    print(message.status)
