
import json
import requests

# Data from the first API
api_response = {
    "itemName": "Brilliant Molten Cloak",
    "nbtData": {
        "data": {
            "attributes": {
                "veteran": 7,
                "mana_pool": 5
            },
            "uid": "8cea07b4a2db",
            "boss_tier": 4,
            "uuid": "c8d16eae-b6e4-4479-b16d-8cea07b4a2db"
        }
    },
    "flatNbt": {
        "veteran": "7",
        "mana_pool": "5",
        "uid": "8cea07b4a2db",
        "boss_tier": "4",
        "uuid": "c8d16eae-b6e4-4479-b16d-8cea07b4a2db"
    },
    "auctioneerId": "534e7e9e05574c0187231374cb0185ce"
}

# Construct the request body for the second API
request_body = {
    "chestName": api_response["itemName"],  # Use itemName for chestName
    "fullInventoryNbt": json.dumps(api_response["flatNbt"]),  # Serialize flatNbt
    "jsonNbt": json.dumps(api_response["nbtData"]),  # Serialize nbtData
    "senderContactId": api_response["auctioneerId"]  # Use auctioneerId
}

# Make the API call
url = "https://example.com/second-api"  # Replace with the actual endpoint
headers = {"Content-Type": "application/json"}
response = requests.post(url, headers=headers, json=request_body)

# Handle the response
if response.status_code == 200:
    print("API call successful:", response.json())
else:
    print("API call failed:", response.status_code, response.text)
