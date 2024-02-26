import requests

API_URL = "http://ccduit.example.com/api"
headers = {"Content-Type": "application/json"}

interaction_data = {
    "InitiatedBy": "urn:ngsi-ld:fedC:communityC1",
    "sourceFederation": "urn:ngsi-ld:Federation:B",
    "targetFederation": "urn:ngsi-ld:Federation:C",
    "sourcedataModel": "urn:data_model:transportation:GTFS",
    "targetdataModel": "urn:data_model:transportation:NGSI-LD",
    "fromCommunity": "urn:ngsi-ld:fedB:communityB3",
    "ToCommunity": "urn:ngsi-ld:fedC:communityC1",
    "SourceSpecificPath": "/GTFS/rawdata",
    "TargetSpecificPath": "/data/CreateEntities",
    "ConnectionType":"DataExchange",
    "ConnectionStatus": "Initiating",
    "customFunction": "urn:ngsi-ld:gtfs2ngsi-ldconverter:a12"
}
response = requests.post(API_URL + "/interactions/createInteraction", json=interaction_data, headers=headers)
assert response.status_code == 200  # Success
