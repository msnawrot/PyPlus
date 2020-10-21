from netmiko import *
from getpass import getpass
import datetime

password = getpass("Type in the password:  ")

# nxos1 (NX-OSv Switch)
nxos1 = {
    'host' : 'nxos1.lasthop.io',
    'username' : 'pyclass',
    'password' : password,
    'device_type' : 'cisco_nxos'
}
# nxos2 (NX-OSv Switch)
nxos2 = {
    'host' : 'nxos2.lasthop.io',
    'username' : 'pyclass',
    'password' : password,
    'device_type' : 'cisco_nxos'
}

routers = [nxos1, nxos2]

for router in routers:
    begin = datetime.datetime.now()
    net_connect = ConnectHandler(**router)
    output = net_connect.send_config_from_file('make_vlans.txt')
    if len(output) > 0:
        print(output)
        print(f"successfully sent config to device, {router['host']}.")
    if net_connect.save_config():
        print(f"successfully saved to startup config on {router['host']}.")
    net_connect.disconnect()
    end = datetime.datetime.now()
    elapsed = end - begin
    print("It took this long to complete. : ", elapsed)
