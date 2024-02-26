import requests

API_URL = "http://ccduit.example.com/api"
headers = {"Content-Type": "application/json"}


response = requests.get(API_URL + "/entities?type=DataModel&DataTypes=BuildingData", headers=headers)
assert response.status_code == 200  # Success
Transportation_data_types_ids = response.json()  # Contains information about Federation B and others

for id in Transportation_data_types_ids:
    response = requests.get(API_URL + "/entities?type=Community&DataTypes=Community&partOfFederation=urn:ngsi-ld:Federation:B&HasDataModels="+id+"", headers=headers)
    assert response.status_code == 200  # Success
    Transportation_data_locations = response.json()  # Contains information about Federation B communities that have data of interest

