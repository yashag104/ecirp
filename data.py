import requests
import random


category_list = [9, 17, 18, 22, 23, 24]
parameters = {
    "amount": 10,
    "type": "boolean",
    "category": random.choice(category_list)
}
response = requests.get(url="https://opentdb.com/api.php", params=parameters)
question_data = response.json()["results"]

