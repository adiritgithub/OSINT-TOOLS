import requests

# Function to get IP address details including coordinates
def get_ip_info(ip_address):
    api_url = f"http://ip-api.com/json/103.121.153.61"
    response = requests.get(api_url)
    ip_info = response.json()
    return ip_info

# Function to simulate Browserleaks-like information (basic browser fingerprinting)
def get_browser_info():
    import platform
    import sys

    browser_info = {
        "OS": platform.system(),
        "OS Version": platform.version(),
        "Architecture": platform.machine(),
        "Python Version": sys.version,
        "User Agent": requests.get('https://httpbin.org/user-agent').json()['user-agent']
    }
    return browser_info

# Main function to print full information
def main(ip_address):
    ip_info = get_ip_info(ip_address)
    browser_info = get_browser_info()

    print("IP Address Information:")
    print(f"IP: {ip_info.get('query')}")
    print(f"Country: {ip_info.get('country')}")
    print(f"Region: {ip_info.get('regionName')}")
    print(f"City: {ip_info.get('city')}")
    print(f"ZIP Code: {ip_info.get('zip')}")
    print(f"Latitude: {ip_info.get('lat')}")
    print(f"Longitude: {ip_info.get('lon')}")
    print(f"ISP: {ip_info.get('isp')}")
    print(f"Org: {ip_info.get('org')}")
    print(f"Timezone: {ip_info.get('timezone')}")
    print(f"AS: {ip_info.get('as')}")

    print("\nBrowser Information (similar to Browserleaks):")
    for key, value in browser_info.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    # Example IP address, you can replace it with any other
    ip_address = "8.8.8.8"
    main(ip_address)
