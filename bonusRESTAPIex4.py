import os
import requests
from urllib3.exceptions import InsecureRequestWarning
from pprint import pprint

requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

if __name__ == "__main__":
    print("*" * 10)
    print("\nRetreiving all devices.\n")
    http_headers = {}
    http_headers['Content-Type'] = "application/json; version=2.4;"
    http_headers['accept'] = "application/json; version=2.4;"
    token = os.environ["NETBOX_TOKEN"]
    http_headers['Authorization'] = f"Token {token}"
    url = "https://netbox.lasthop.io/api/ipam/ip-addresses/"
    post_data = { "address": "192.0.2.100/32"}

    response = requests.post(url, headers=http_headers, data=post_data, verify=False)
    print("RESPONSE CODE:", response.status_code)
    print("RESPONSE DATA:", response.json())
