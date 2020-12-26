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


# Run the following two show commands on the nxos1 device using a single method
# and passing in a list of commands: "show system uptime" and "show system
# resources"
my_cmds = ["interface loopback 126", "loopback interface 127"]
raw_output = device.config_list(my_cmds)
# Print the XML output from these two commands.
for entry in raw_output:
    print(etree.tostring(entry).decode())
