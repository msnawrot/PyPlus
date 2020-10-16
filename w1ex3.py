from netmiko import ConnectHandler
from getpass import getpass

nxos1 = {
    'device_type': 'cisco_nxos',
    'host': 'nxos1.lasthop.io',
    'username': 'pyclass',
    'password': getpass('Password for nxos1: '),
}

routers = [nxos1]

for router in routers:
    c = ConnectHandler(**router, session_log = './w1ex3.log.txt')
    c.send_command('show version')
