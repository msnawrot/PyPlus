import pyeapi
from getpass import getpass

connection = pyeapi.client.connect(
    transport="https",
    host="arisa3.lasthop.io",
    username="pyclass",
    password=getpass(),
    port="443",
)

show_cmd = "show ip arp"

device = pyeapi.client.Node(connection)
output = device.enable(show_cmd)
print(output)
#  From this ARP table data, print out a mapping of all of the IP addresses and
# their corresponding MAC addresses.
