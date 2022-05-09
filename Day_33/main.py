import requests
from datetime import datetime
import smtplib
import time

MY_EMAIL = ""
PASSWORD = ""
MY_LAT = 19.974869
MY_LONG = -99.171932


def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_longitude = float(data["iss_position"]["longitude"])
    iss_latitude = float(data["iss_position"]["latitude"])

    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_longitude <= MY_LONG+5:
        return True


def is_night():
    # parameters = {
    #     "lat": MY_LAT,
    #     "lng": MY_LONG,
    #     "formatted": 0
    # }
    # response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    # response.raise_for_status()
    # data = response.json()
    sunrise = 7  # int(data['results']['sunrise'].split("T")[1].split(":")[0])
    sunset = 19  # int(data['results']['sunset'].split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    if time_now >= sunset or time_now <= sunrise:
        return True


while True:
    time.sleep(60)
    if is_iss_overhead():  # and is_night()
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()  # make the connection secure
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=MY_EMAIL,
                msg="Subject:Look Up👆\n\nThe ISS is above you in the sky."
            )
        print("Successfully sent")
