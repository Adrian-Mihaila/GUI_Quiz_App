import requests

parameters = {
    "amount": 100,
    "type": "boolean"
}

response = requests.get(url="https://opentdb.com/api.php", params=parameters)  # Without params the var will be empty
response.raise_for_status()  # Handling errors and gives feedback
data = response.json()  # converts in json
question_data = data["results"]
