import os
import requests
from urllib3.exceptions import InsecureRequestWarning
from pprint import pprint

requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

if __name__ == "__main__":
    http_headers = {}
    http_headers['accept'] = "application/json; version=2.4;"
    print("*" * 10)
    print("\nRetreiving all devices.\n")
    url = "https://netbox.lasthop.io/api/dcim/devices/"
    token = os.environ["NETBOX_TOKEN"]
    http_headers['Authorization'] = f"Token {token}"
    response = requests.get(url, headers=http_headers, verify=False)
    tempresults = response.json()
    results = tempresults['results']

    for device in results:
        print(device['display_name'])
