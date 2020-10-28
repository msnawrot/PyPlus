from netmiko import *
import yaml

with open(".netmiko.yml") as f:
    yaml_out = yaml.load(f, Loader=yaml.FullLoader)

net_connect = ConnectHandler(**yaml_out['cisco4'])
print(net_connect.send_command("show run"))
