import requests

API_URL = "http://ccduit.example.com/api"
headers = {"Content-Type": "application/json"}

policy_data = { ... }  # Defined previously


# Storing Policy Model
response = requests.post(API_URL + "/admin/CreatePolicy/", json=policy_data, headers=headers)
assert response.status_code == 201  # Success
