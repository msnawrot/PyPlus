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
        temphostname = device['display_name']
        temploc = device['site']['name']
        tempvendor = device['device_type']['manufacturer']['name']
        tempstatus = device['status']['label']
        print("-" * 60 )
        print(temphostname)
        print("-" * 10 )
        print("Location:", temploc)
        print("Vendor:", tempvendor)
        print("Status:", tempstatus)
        print("-" * 60 )
        print("\n\n")
