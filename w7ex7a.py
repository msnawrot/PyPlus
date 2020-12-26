import requests # b/c want disable cert warning on self-signed certs
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from getpass import getpass
from nxapi_plumbing import Device
from lxml import etree

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

# Create an nxapi_plumbing "Device" object for nxos1
device = Device(
    api_format= "xml",
    transport= "https",
    port=8443,
    host='nxos1.lasthop.io',
    verify=False,
    username='pyclass',
    password=getpass()
)

# Send the "show interface Ethernet1/1" command to the device
raw_output = device.show("show interface Ethernet1/1")
# parse the output
int_name = raw_output[0][0][0].find("interface").text
int_state = raw_output[0][0][0].find("state").text
int_mtu = raw_output[0][0][0].find("eth_mtu").text


# print out the following information:
print("Interface:", int_name + "; State:", int_state + "; MTU:", int_mtu)
