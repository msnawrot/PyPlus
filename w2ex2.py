from netmiko import *
from getpass import getpass
import datetime

nxos2 = {
    'host': 'nxos2.lasthop.io',
    'username': 'pyclass',
    'device_type': 'cisco_nxos',
    'password': getpass("Password: "),
    'global_delay_factor': 2
}

connection=ConnectHandler(**nxos2)
start1 = datetime.datetime.now()
output1 = connection.send_command("show lldp neighbors detail")
print(output1)
end1 = datetime.datetime.now()
elapsed1 = end1 - start1
print(elapsed1)

start2 = datetime.datetime.now()
output2 = connection.send_command("show lldp neighbors detail", delay_factor=8)
print(output2)
end2 = datetime.datetime.now()
elapsed2 = end2 - start2
print(elapsed2)
connection.disconnect()
