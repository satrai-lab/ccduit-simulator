import requests

API_URL = "http://ccduit.example.com/api"
headers = {"Content-Type": "application/json"}


response = requests.get(API_URL + "/entities?type=CustomFunction&DataModelMap[From=urn:data_model:transportation:GTFS,To=urn:data_model:transportation:NGSI-LD]", headers=headers)
assert response.status_code == 200  # Success
Custom_Function = response.json()  # Contains information about the converter function code





