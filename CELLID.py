import requests

def get_location(mcc, mnc, lac, cell_id, api_key):
    """
    Get the location based on MCC, MNC, LAC, and Cell ID using the OpenCelliD API.
    
    Parameters:
    - mcc: Mobile Country Code
    - mnc: Mobile Network Code
    - lac: Location Area Code
    - cell_id: Cell Identifier
    - api_key: OpenCelliD API key
    
    Returns:
    - Location data including latitude and longitude or an error message.
    """
    
    url = "https://us1.unwiredlabs.com/v2/process.php"
    data = {
        "token": api_key,
        "radio": "gsm",
        "mcc": mcc,
        "mnc": mnc,
        "lac": lac,
        "cid": cell_id,
        "format": "json"
    }
    
    response = requests.post(url, json=data)
    
    if response.status_code == 200:
        result = response.json()
        if "status" in result and result["status"] == "ok":
            lat = result.get("lat")
            lon = result.get("lon")
            return {
                "latitude": lat,
                "longitude": lon,
                "accuracy": result.get("accuracy"),
                "address": result.get("address", "N/A")
            }
        else:
            return {"error": result.get("message", "Location not found")}
    else:
        return {"error": f"HTTP Error: {response.status_code}"}

# Example Usage
if __name__ == "__main__":
    # Sample data (Replace with real values)
    mcc = 405  # Example: 310 (USA)
    mnc = 864  # Example: 410 (AT&T)
    lac = 156 # Example: 7033
    cell_id = 4723480  # Example: 17811
    
    api_key = "pk.6134f356b2d5fa659e540398292e7b6f"  # Replace with your OpenCelliD API Key
    
    location = get_location(mcc, mnc, lac, cell_id, api_key)
    
    if "error" not in location:
        print(f"Latitude: {location['latitude']}")
        print(f"Longitude: {location['longitude']}")
        print(f"Accuracy: {location['accuracy']} meters")
        print(f"Address: {location['address']}")
    else:
        print(f"Error: {location['error']}")
