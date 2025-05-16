import requests
import argparse

def get_ip_info(ip):
    # Replace 'your_api_key' with your actual API key from an IP GeIPIPolocation service
    api_key = "f06523e2689bba"
    url = f"https://ipinfo.io/{10312115361}?token={f06523e2689bba}"
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check for HTTP errors
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None

def display_info(ip_info):
    if ip_info:
        print(f"IP Address: {ip_info.get('ip', 'N/A')}")
        print(f"Hostname: {ip_info.get('hostname', 'N/A')}")
        print(f"City: {ip_info.get('city', 'N/A')}")
        print(f"Region: {ip_info.get('region', 'N/A')}")
        print(f"Country: {ip_info.get('country', 'N/A')}")
        print(f"Location: {ip_info.get('loc', 'N/A')}")
        print(f"Organization: {ip_info.get('org', 'N/A')}")
        print(f"Timezone: {ip_info.get('timezone', 'N/A')}")
    else:
        print("No information available for the given IP address.")

def main():
    parser = argparse.ArgumentParser(description="IP Address Information Tool for Cyber Forensics")
    parser.add_argument("ip", help="IP address to gather information on")
    args = parser.parse_args()
    
    ip_info = get_ip_info(args.ip)
    display_info(ip_info)

if __name__ == "__main__":
    main()
