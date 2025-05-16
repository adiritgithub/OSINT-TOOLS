import requests
import argparse
import platform
import sys

# Function to get IP address details including geolocation and ISP info
def get_ip_info(ip):
    # Using ipinfo.io API for geolocation data
    api_key = "f06523e2689bba"  # Replace with your actual API key from ipinfo.io
    url = f"https://ipinfo.io/103.121.153.61?token={f06523e2689bba}"
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check for HTTP errors
        ip_info = response.json()
        return ip_info
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None

# Function to simulate Browserleaks-like information (basic browser fingerprinting)
def get_browser_info():
    user_agent = requests.get('https://httpbin.org/user-agent').json()['user-agent']
    browser_info = {
        "OS": platform.system(),
        "OS Version": platform.version(),
        "Architecture": platform.machine(),
        "Python Version": sys.version,
        "User Agent": user_agent
    }
    return browser_info

# Function to display IP information
def display_ip_info(ip_info):
    if ip_info:
        print("IP Address Information:")
        print(f"IP: {ip_info.get('ip', 'N/A')}")
        print(f"Hostname: {ip_info.get('hostname', 'N/A')}")
        print(f"City: {ip_info.get('city', 'N/A')}")
        print(f"Region: {ip_info.get('region', 'N/A')}")
        print(f"Country: {ip_info.get('country', 'N/A')}")
        print(f"Location: {ip_info.get('loc', 'N/A')}")
        print(f"Organization: {ip_info.get('org', 'N/A')}")
        print(f"Timezone: {ip_info.get('timezone', 'N/A')}")
        print(f"Postal Code: {ip_info.get('postal', 'N/A')}")
    else:
        print("No information available for the given IP address.")

# Function to display browser information
def display_browser_info(browser_info):
    print("\nBrowser Information (similar to Browserleaks):")
    for key, value in browser_info.items():
        print(f"{key}: {value}")

# Main function to integrate all functionality
def main():
    parser = argparse.ArgumentParser(description="Advanced IP Geolocation and Browser Information Tool for Cyber Forensics")
    parser.add_argument("ip", help="IP address to gather information on")
    args = parser.parse_args()
    
    ip_info = get_ip_info(args.ip)
    browser_info = get_browser_info()
    
    display_ip_info(ip_info)
    display_browser_info(browser_info)

if __name__ == "__main__":
    main()
