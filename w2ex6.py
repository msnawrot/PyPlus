from netmiko import ConnectHandler, file_transfer
from getpass import getpass
import time 

password = getpass()
device = {
    "host": "cisco4.lasthop.io",
    "username": "pyclass",
    "password": password,
    "secret": password,
    "device_type": "cisco_ios",
    "session_log": "my_output.txt"
}

# open an ssh session with netmiko
ssh_conn = ConnectHandler(**device)
print(ssh_conn.find_prompt())
print(ssh_conn.config_mode())
print(ssh_conn.find_prompt())
print(ssh_conn.exit_config_mode())
print(ssh_conn.find_prompt())
print(ssh_conn.write_channel('disable\n'))
print("Waiting two seconds...")
time.sleep(2.0)
print(ssh_conn.read_channel())
print(ssh_conn.enable()) #this method requires the secret key in the device dictionary
print(ssh_conn.find_prompt())
print(ssh_conn.disconnect())
print("Remember to look at my_output.txt file!!")
