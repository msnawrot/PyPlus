from my_funcs import read_yaml
from my_funcs import run_show_command

device_dict = read_yaml('w6ex2a.yml')
device_dict['password'] = getpass("password please: ")
show_cmd = "show ip route"
run_show_command(**device_dict, show_cmd)
