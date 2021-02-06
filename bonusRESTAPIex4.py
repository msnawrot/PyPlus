import os
import requests
from urllib3.exceptions import InsecureRequestWarning
from pprint import pprint
import json

requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

if __name__ == "__main__":
    print("*" * 10)
    http_headers = {}
    http_headers['Content-Type'] = "application/json; version=2.4;"
    http_headers['accept'] = "application/json; version=2.4;"
    token = os.environ["NETBOX_TOKEN"]
    http_headers['Authorization'] = f"Token {token}"
    url = "https://netbox.lasthop.io/api/ipam/ip-addresses/"
    post_data = { "address": "192.0.2.101/32"}

    response = requests.post(url, headers=http_headers, data=json.dumps(post_data), verify=False)
    print("RESPONSE CODE:", response.status_code)
    print("RESPONSE DATA:", response.text)

# {"id":277,"family":4,"address":"192.0.2.100/32","vrf":null,"tenant":null,"status":{"value":1,"label":"Active"},"role":null,"interface":null,"description":"","nat_inside":null,"nat_outside":null,"tags":[],"custom_fields":{},"created":"2021-01-27","last_updated":"2021-01-27T16:46:37.742458-08:00"}
