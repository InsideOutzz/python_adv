import requests

# URL for the FastAPI endpoint
api_url = "http://127.0.0.1:8000/create_person"

# Data to be sent in the request
person_data = {"name": "John Doe", "age": 30}

# Send a POST request to the FastAPI endpoint
response = requests.post(api_url, json=person_data)

# Print the response
print("Response Code:", response.status_code)
print("Response JSON:", response.json())