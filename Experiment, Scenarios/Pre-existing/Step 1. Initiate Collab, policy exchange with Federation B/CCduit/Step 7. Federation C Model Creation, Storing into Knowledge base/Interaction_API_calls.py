import requests

API_URL = "http://ccduit.example.com/api"
headers = {"Content-Type": "application/json"}

federation_data = { ... }  # Defined previously
community_data = { ... }  # Defined previously
Data_model_data = { ... } # Defined Previously

# Storing Federation Model
response = requests.post(API_URL + "/entities/", json=federation_data, headers=headers)
assert response.status_code == 201  # Success

# Storing Community Model
response = requests.post(API_URL + "/entities/", json=community_data, headers=headers)
assert response.status_code == 201  # Success

# Storing Community Model
response = requests.post(API_URL + "/entities/", json=Data_model_data, headers=headers)
assert response.status_code == 201  # Success