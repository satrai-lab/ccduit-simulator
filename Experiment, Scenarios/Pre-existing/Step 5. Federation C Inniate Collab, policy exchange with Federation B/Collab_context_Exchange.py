import requests

API_URL = "http://ccduit.example.com/api"
headers = {"Content-Type": "application/json"}

Context_exchange_request1 = {
  "targetFederation": "urn:ngsi-ld:Federation:B",
  "Context": "[Data Model,community,federation,Function]"
}

response = requests.post(API_URL + "/admin/contextExchange/", json=Context_exchange_request1, headers=headers)
assert response.status_code == 200  # Success

Context_exchange_request2 = {
  "targetFederation": "urn:ngsi-ld:Federation:A",
  "Context": "[Data Model,community,federation,Function]"
}

response = requests.post(API_URL + "/admin/contextExchange/", json=Context_exchange_request2, headers=headers)
assert response.status_code == 200  # Success