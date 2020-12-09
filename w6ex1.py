import pyeapi
from getpass import getpass

connection = pyeapi.client.connect(
    transport="https",
    host="arista3.lasthop.io",
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


# convert output to a list of tuples
ip_mac_list = list()
for addr_dict in output[0]['result']['ipV4Neighbors']:
    print(addr_dict)
    ip_addr = addr_dict['address']
    mac_addr = addr_dict['hwAddress']
    ip_mac_list.append((ip_addr, mac_addr))

# print the list of tuples with a for loop
print("IP Address\tMAC Address")
for ip_addr, mac_addr in ip_mac_list:
    print(ip_addr, "\t", mac_addr)
