from netmiko import ConnectHandler
from getpass import getpass

nxos1 = {
    'device_type': 'cisco_nxos',
    'host': 'nxos1.lasthop.io',
    'username': 'pyclass',
    'password': getpass('Password for nxos1: '),
    'session_log': './w1ex3.nxos1.log.txt'
}

nxos2 = {
  'device_type': 'cisco_nxos',
  'host': 'nxos2.lasthop.io',
  'username': 'pyclass',
  'password': getpass(),
  'session_log': './w1ex3.nxos2.log.txt'
}

routers = [nxos1, nxos2]

for router in routers:
    c = ConnectHandler(**router)
    c.send_command('show version')
