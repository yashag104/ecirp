import requests
from datetime import datetime
import os


APP_ID = os.environ["NIX_APP_ID"]
API_KEY = os.environ["NIX_APP_KEY"]
USERNAME = os.environ["SHEETY_USERNAME"]
TOKEN = "asdfghjklqwertyuiopzxcvbnm"

date = datetime.now().date().strftime("%d/%m/%Y")
time = datetime.now().time().strftime("%H:%M:%S")

data_endpoint = "https://api.sheety.co/1c0343f4bcd63ac368920a06ace5d27b/healthout/sheet1"
exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
nutrients_endpoint = "https://trackapi.nutritionix.com/v2/natural/nutrients"

parameter = {
    "query": str(input("What did you do today? ")),
    "gender": "male",
    "weight_kg": "103",
    "height_cm": "180",
    "age": "19"
}

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "x-remote-user-id": "0",
}

exercise_response = requests.post(url=exercise_endpoint, json=parameter, headers=headers)
exercise_info = exercise_response.json()["exercises"][0]

exercise_data = {
    "sheet1": {
        "date": date,
        "time": time,
        "activity": exercise_info["name"].title(),
        "duration": exercise_info["duration_min"],
        "calories": exercise_info["nf_calories"]
     }
}

data_response = requests.post(
    data_endpoint,
    json=exercise_data,
    auth=(
        os.environ["SHEETY_USERNAME"],
        os.environ["SHEETY_PASSWORD"]
    )
)
print(data_response.status_code, exercise_response.status_code)
