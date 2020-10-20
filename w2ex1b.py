from netmiko import *
from getpass import getpass

router = {
    'device_type': 'cisco_ios',
    'host': 'cisco4',
    'username': 'pyclass',
    'password': getpass('Password for router: ')
}

connection = ConnectHandler(**router)
output = connection.send_command('ping', expect_string=r'col \[ip\]:')
output += connection.send_command('\n', expect_string=r'Target IP address: ')
output += connection.send_command('8.8.8.8', expect_string=r'Repeat count \[5\]: ')
output += connection.send_command('\n', expect_string=r'Datagram size \[100\]:')
output += connection.send_command('\n', expect_string=r'Timeout in seconds \[2\]: ')
output += connection.send_command('\n', expect_string=r'Extended commands \[n\]: ')
output += connection.send_command('\n', expect_string=r'Sweep range of sizes \[n\]:')
output += connection.send_command('\n', expect_string=r'#')
