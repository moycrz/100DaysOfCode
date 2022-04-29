import requests
from datetime import datetime
import os

APP_ID = os.getenv("APP_ID")
API_KEY = os.getenv("API_KEY")

SHEETY_USER_NAME = os.getenv("USER_NAME")
SHEETY_PASSWORD = os.getenv("PASSWORD")

GENDER = "male"
WEIGHT_KG = "75"
HEIGHT_CM = "178"
AGE = "23"

api_exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
header = {
    "x-app-key": API_KEY,
    "x-app-id": APP_ID,
}
user_query = input("Tell me wich exercise you did: ")

parameters = {
    "query": user_query,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE,
}

response = requests.post(url=api_exercise_endpoint, json=parameters, headers=header)
response.raise_for_status()
result = response.json()
# name_exercise = [result["exercises"][i]["name"].title() for i in range(len(result["exercises"]))]
# duration_exercise = [result["exercises"][i]["duration_min"] for i in range(len(result["exercises"]))]
# calories_exercise = [result["exercises"][0]["nf_calories"] for i in range(len(result["exercises"]))]

today = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

sheety_endpoint = os.getenv("SHEET_ENDPOINT")

sheety_header = {
    "Authorization": f"Basic {SHEETY_PASSWORD}"
}

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    response = requests.post(url=sheety_endpoint, json=sheet_inputs, headers=sheety_header)
    # response.raise_for_status()
    print(response.text)

