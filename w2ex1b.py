from netmiko import *
from getpass import getpass

router = {
    'device_type': 'cisco_ios',
    'host': 'cisco4.lasthop.io',
    'username': 'pyclass',
    'password': getpass('Password for router: ')
}

connection = ConnectHandler(**router)
output = connection.send_command('ping', expect_string=r'col \[ip\]:', strip_prompt=False, strip_command=False)
output += connection.send_command('\n', expect_string=r'Target IP address: ', strip_prompt=False, strip_command=False)
output += connection.send_command('8.8.8.8', expect_string=r'Repeat count \[5\]: ', strip_prompt=False, strip_command=False)
output += connection.send_command('\n', expect_string=r'Datagram size \[100\]:', strip_prompt=False, strip_command=False)
output += connection.send_command('\n', expect_string=r'Timeout in seconds \[2\]: ', strip_prompt=False, strip_command=False)
output += connection.send_command('\n', expect_string=r'Extended commands \[n\]: ', strip_prompt=False, strip_command=False)
output += connection.send_command('\n', expect_string=r'Sweep range of sizes \[n\]:', strip_prompt=False, strip_command=False)
output += connection.send_command('\n', expect_string=r'#', strip_prompt=False, strip_command=False)
print(output)
