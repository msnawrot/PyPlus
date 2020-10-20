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
pprint(net_connect.send_command('show lldp neighbors', use_textfsm=True))
