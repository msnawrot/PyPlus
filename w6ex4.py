from my_funcs import read_yaml
from my_funcs import run_show_command
from getpass import getpass

devices = read_yaml('w6ex4.yml')
device_dict['password'] = getpass("password please: ")

for switch in devices:
    print(switch.keys())
connection = pyeapi.client.connect(**device)
device = pyeapi.client.Node(connection)
output = device.enable(cmd)

show_cmd = "show ip interface brief"
result = run_show_command(show_cmd,**device_dict)
