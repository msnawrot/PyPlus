from netmiko import *
from getpass import getpass
import datetime

nsox2 = {
    'hostname': 'nxos2.lasthop.io',
    'username': 'pyclass',
    'device_type': 'cisco_nxos',
    'password': getpass("Password: ")
}

connection=ConnectHandler(**nxos2, global_delay_factor=2)
start1 = datetime.datetime.now()
output1 = connection.send_command("show lldp neighbors detail")
print(output1)
end1 = datetime.datetime.now()
elapsed1 = end1 - start1
elapsed1 = divmod(elapsed.days * 86400 + elapsed.seconds, 60)
print('Process completed in %s minutes %s seconds' % (str(elapsed1[0]), str(elapsed1[1])))

start2 = datetime.datetime.now()
output2 = connection.send_command("show lldp neighbors detail", delay_factor=8)
print(output2)
end2 = datetime.datetime.now()
elapsed2 = end2 - start2
elapsed2 = divmod(elapsed.days * 86400 + elapsed.seconds, 60)
print('Process completed in %s minutes %s seconds' % (str(elapsed2[0]), str(elapsed2[1])))
connection.disconnect()
