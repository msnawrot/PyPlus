import yaml
import pyeapi
from getpass import getpass

filename = "w6ex2a.yml"
with open(filename) as f:
    yaml_out = yaml.load(f, Loader=yaml.FullLoader)

device_dict = yaml_out

device_dict['password'] = getpass("password please: ")
connection = pyeapi.client.connect(**device_dict)

show_cmd = "show ip arp"

device = pyeapi.client.Node(connection)
output = device.enable(show_cmd)
#  From this ARP table data, print out a mapping of all of the IP addresses and
# their corresponding MAC addresses.


# convert output to a list of tuples
ip_mac_list = list()
for addr_dict in output[0]['result']['ipV4Neighbors']:
    ip_addr = addr_dict['address']
    mac_addr = addr_dict['hwAddress']
    ip_mac_list.append((ip_addr, mac_addr))

# print the list of tuples with a for loop
print("IP Address\t MAC Address")
for ip_addr, mac_addr in ip_mac_list:
    print(ip_addr, "\t", mac_addr)
