from netmiko import *
import getpass
import datetime

router = {
    'device_type': 'cisco_ios',
    'host': 'cisco3.lasthop.io',
    'username': 'pyclass',
    'password': getpass('Password for router: ')
}

cfg = [
    'ip name-server 1.2.1.1',
    'ip name-server 1.2.0.1',
    'ip domain-lookup'
]
start1 = datetime.datetime.now()
net_connect = ConnectHandler(**router)
output = net_connect.send_config_set(cfg)
end1 = datetime.datetime.now()
elapsed1 = end1 - start1
print(elapsed1)
print(output)
