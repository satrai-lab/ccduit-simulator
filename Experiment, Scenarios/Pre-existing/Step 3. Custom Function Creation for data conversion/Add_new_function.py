import requests

API_URL = "http://ccduit.example.com/api"
headers = {"Content-Type": "application/json"}

Function_data = { "id": "urn:ngsi-ld:gtfs2ngsi-ldconverter:a12",
                  "type":"Custom Function",
                  "name": {
                      "type": "Property",
                      "value": "BRICKtoNGSILDConverter"
                  },
                  "DataModelMap":{
                      "type":"Relationship",
                      "object":{
                          "From":"urn:data_model:transportation:GTFS",
                          "To":"To=urn:data_model:transportation:NGSI-LD"
                      }
                  },
                  "CCduit_compatible": {
                      "type": "Property",
                      "value": "YES"
                  },
                  "Code": {
                      "type": "Property",
                      "value": {"CODE ALREADY DEFINED IN CONVERTER.py"}
                  },
                  "@context": ["DOUBLEBLINDREVIEW"]
                  
                  }

# Storing Federation Model
response = requests.post(API_URL + "/entities/", json=Function_data, headers=headers)
assert response.status_code == 201  # Success