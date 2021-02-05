import requests
from urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

if __name__ == "__main__":
    url = "https://netbox.lasthop.io/api/"
    http_headers = {"accept": "application/json; version=2.4;"}
    # if token:
    #     http_headers["authorization"] = "Token {}".format(token)

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
