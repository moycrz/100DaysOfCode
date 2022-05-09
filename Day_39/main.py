from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
user_data = data_manager.get_user_data()
flight_search = FlightSearch()
notification_manager = NotificationManager()

ORIGIN_CITY_IATA = "LON"

print("Welcome to Moises's Flight Club.\nWe find the best flight deals and email you.")
user_name = input("What is your first name? ")
user_lastname = input("What is your last name? ")
user_email = input("What is your email? ")
user_email_check = input("Type your email again. ")
check_email = data_manager.check_user_data(name=user_name, lastname=user_lastname, email=user_email)
if check_email:
    print("You're in the club!")

    if sheet_data[0]["iataCode"] == "":
        for row in sheet_data:
            row["iataCode"] = flight_search.get_destination_codes(row["city"])
        data_manager.destination_data = sheet_data
        data_manager.update_destination_codes()

    tomorrow = datetime.now() + timedelta(days=1)
    six_month_from_today = datetime.now() + timedelta(days=(6 * 30))
    for user in user_data:
        for destination in sheet_data:
            flight = flight_search.check_flights(
                ORIGIN_CITY_IATA,
                destination["iataCode"],
                from_time=tomorrow,
                to_time=six_month_from_today
            )
            if flight.price < destination["lowestPrice"]:
                msg = f"Low price alert! Only £{flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to"\
                      f" {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to"\
                      f" {flight.return_date}."
                notification_manager.send_sms(
                    message=msg
                )
                notification_manager.send_email(
                    message=msg,
                    to=user["email"]
                )
else:
    print("Successfully! Your email has been added")
