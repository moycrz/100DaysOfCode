import requests

SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/aa679f0a220502d9c0d38f26a024594b/flightDeals/prices"
SHEETY_USERS_ENDPONT = "https://api.sheety.co/aa679f0a220502d9c0d38f26a024594b/flightDeals/users"


class DataManager:

    def __init__(self):
        self.destination_data = {}
        self.user_data = {}

    def get_destination_data(self):
        response = requests.get(url=SHEETY_PRICES_ENDPOINT)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data
            )
            print(response.text)

    def get_user_data(self):
        response = requests.get(url=SHEETY_USERS_ENDPONT)
        data = response.json()
        self.user_data = data["users"]
        return self.user_data

    def check_user_data(self, name, lastname, email):
        for user in self.user_data:
            if user["email"] == email:
                return True
            else:
                self.update_user_data(name, lastname, email)

    def update_user_data(self, name, lastname, email):
        new_data = {
            "users": {
                "fistName": name,
                "lastName": lastname,
                "email": email
            }
        }
        response = requests.put(
            url=f"{SHEETY_USERS_ENDPONT}",
            json=new_data
        )
        print(response.text)

    def get_customer_emails(self):
        customers_endpoint = SHEET_USERS_ENDPOINT
        response = requests.get(customers_endpoint)
        data = response.json()
        self.customer_data = data["users"]
        return self.customer_data