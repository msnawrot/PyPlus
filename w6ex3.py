import my_funcs

device_dict = my_func.read_yaml('w6ex2a.yml')
device_dict['password'] = getpass("password please: ")
show_cmd = "show ip route"
my_funcs.run_show_command(show_cmd,**device_dict)
