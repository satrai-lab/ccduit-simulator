import requests

API_URL = "http://ccduit.example.com/api"
headers = {"Content-Type": "application/json"}

policy_exchange_request = {
  "targetFederation": "urn:ngsi-ld:Federation:B",
  "policyId": "urn:ngsi-ld:ContextPolicy:002"
}

response = requests.post(API_URL + "/admin/policyExchange/", json=policy_exchange_request, headers=headers)
assert response.status_code == 200  # Success