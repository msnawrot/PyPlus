from netmiko import ConnectHandler
from getpass import getpass

nxos1 = {
  'device_type': 'cisco_nxos',
  'host': 'nxos1.lasthop.io',
  'username': 'pyclass',
  'password': '88newclass',
}

nxos2 = {
  'device_type': 'cisco_nxos',
  'host': 'nxos2.lasthop.io',
  'username': 'pyclass',
  'password': '88newclass',
}

routers = [nxos1, nxos2]
for i in routers:
    c = ConnectHandler(**i)
    print(c.find_prompt())
    
