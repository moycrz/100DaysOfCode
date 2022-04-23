import smtplib
from random import *
import datetime as dt

MY_EMAIL = "moises.crza@gmail.com"
PASSWORD = "J@maicanegra2708"
day_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Saturday", "Sunday"]
now = dt.datetime.now()

with open("quotes.txt") as quote_file:
    all_quotes = quote_file.readlines()
    quote = choice(all_quotes)

for i in range(7):
    if now.weekday() == i:
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()  # make the connection secure
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs="moises.c.alcala@gmail.com",
                msg=f"Subject: Happy {day_week[now.weekday()]} :D\n\n{quote}"
            )
    else:
        pass
