import os
import requests
from urllib3.exceptions import InsecureRequestWarning
from pprint import pprint

requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

if __name__ == "__main__":
    url = "https://netbox.lasthop.io/api/"
    http_headers = {}
    http_headers['accept'] = "application/json; version=2.4;"
    response = requests.get(url, headers=http_headers, verify=False)

    # print the HTTP status code, the reesponse text, the json response, and the
    # http response headers.

    print("*" * 10)
    print("HTTP status code:\n")
    print(response.status_code)
    print("\nresponse text:\n")
    print(response.text)
    print("\nresponse json:\n")
    print(response.json())
    print("\nresponse HTTP headers:\n")
    print(response.headers)

    print("*" * 10)
    print("\nRetreiving all endpoints under /api/dcim parent\n")
    url = "https://netbox.lasthop.io/api/dcim/"
    token = os.environ["NETBOX_TOKEN"]
    http_headers['Authorization'] = "Token " + token
    response = requests.get(url, headers=http_headers, verify=False)
    pprint(response.json())
