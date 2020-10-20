from netmiko import *
from getpass import getpass

router = {
    'device_type': 'cisco_ios',
    'host': 'cisco4.lasthop.io',
    'username': 'pyclass',
    'password': getpass('Password for router: ')
}

connection = ConnectHandler(**router)
output = connection.send_command_timing('ping', strip_prompt=False, strip_command=False)
output += connection.send_command_timing('\n', strip_prompt=False, strip_command=False)
output += connection.send_command_timing('8.8.8.8', strip_prompt=False, strip_command=False)
output += connection.send_command_timing('\n', strip_prompt=False, strip_command=False)
output += connection.send_command_timing('\n', strip_prompt=False, strip_command=False)
output += connection.send_command_timing('\n', strip_prompt=False, strip_command=False)
output += connection.send_command_timing('\n', strip_prompt=False, strip_command=False)
output += connection.send_command_timing('\n', strip_prompt=False, strip_command=False)
print(output)
