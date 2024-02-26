# Policy Documentation and Enforcement (Pseudocode)

policies = {
    "federationB": {
        "canReceive": True,
        "canForward": False,
        "allowedDataTypes": ["BuildingData"]
    }
}

def enforce_policy(federation_id, data_type):
    # Check if the data exchange is allowed under the policy
    return policies[federation_id]["canReceive"] and data_type in policies[federation_id]["allowedDataTypes"]