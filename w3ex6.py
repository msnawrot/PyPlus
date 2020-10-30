from netmiko import *
import yaml
from ciscoconfparse import CiscoConfParse

with open("../.netmiko.yml") as f:
    yaml_out = yaml.load(f, Loader=yaml.FullLoader)

net_connect = ConnectHandler(**yaml_out['cisco4'])
showrun = net_connect.send_command("show run")
# showrun should be a list but it is a string, so let's splitlines the string
showrun_list = showrun.splitlines()
# create the cisco_obj
cisco_obj = CiscoConfParse(showrun_list)

ints_w_ip = cisco_obj.find_objects_w_child(parentspec=r"interface", childspec=r"^\s+ip address")
if len(ints_w_ip) == 0:
    print("No interfaces with IP addresses found.")
if len(ints_w_ip) == 1:
    print("Interface Line: ", ints_w_ip[0].text)
    print("IP Address Line: ", ints_w_ip[0].children[0].text)
elif len(ints_w_ip) > 1:
    for i in ints_w_ip:
        print("Interface Line:: ", ints_w_ip[0].text)
        print("IP Address Line: ", ints_w_ip[0].children[0].text)
        print("-" * 10)
