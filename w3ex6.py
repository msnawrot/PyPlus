from netmiko import *
import yaml
from CiscoConfParse import CiscoConfParse

with open("../.netmiko.yml") as f:
    yaml_out = yaml.load(f, Loader=yaml.FullLoader)

net_connect = ConnectHandler(**yaml_out['cisco4'])
showrun = net_connect.send_command("show run")
# showrun should be a list
