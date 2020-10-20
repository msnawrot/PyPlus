from netmiko import *
from getpass import getpass
from pprint import pprint


router = {
    'device_type': 'cisco_ios',
    'host': 'cisco4.lasthop.io',
    'username': 'pyclass',
    'password': getpass('Password for router: ')
}

net_connect = ConnectHandler(**router)
output = net_connect.send_command('show version', use_textfsm=True)
print(type(output))
print(type(output[0]))
print(output)
better_output = net_connect.send_command('show lldp neighbors', use_textfsm=True)
pprint(better_output)
# I need to print out the remote device's interface for the LLDP neighbor.
print("The one LLDP neighbor is named %s and connects via it's interface %s." % (str(better_output['neighbor']), str(better_output['neighbor_interface'])))
