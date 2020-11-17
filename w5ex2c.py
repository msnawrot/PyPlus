# NEW START HERE
# imports
from getpass import getpass
import yaml
from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment
from netmiko import ConnectHandler
from pprint import pprint

# global Variables
# password = getpass("Type in the password for the routers: ")
filename = "testlist2.yml"
with open(filename) as f:
    yaml_out = yaml.load(f, Loader=yaml.FullLoader)

# jinja2 environment
env = Environment(undefined=StrictUndefined)
env.loader = FileSystemLoader([".", "./jinja2"])

# jinja2 templates
j2_template = "w5ex2b_tpl.j2"

def render_config(routers):
    for e in (routers):
        j2_vars = e[0]['j2_vars']
        #print(type(j2_vars))
        #print(j2_vars)
        template = env.get_template(j2_template)
        output = template.render(**j2_vars)
        print(f"rendered config for {j2_vars['host']}:\n", output)
        print("\n")
        print("Storing rendered config...")
        e[1]['nm_vars'].update({'config': output})
        print(e)

render_config(yaml_out)


## push configuration changes function
## router must be a dictionary, with session_log, host, username, password, and device_type keys
## why not have a config key in the dictionary, too

for e in yaml_out:
    nm_vars = e[1]['nm_vars']
    config = nm_vars['config']
    net_connect = ConnectHandler(**net_connect)
    output = net_connect.send_config_set(cfg)
    print(output)


#9)
#storing routers in a dictionary:
#device1 = {
#  'host': 'cisco1.lasthop.io',
#  'username': 'pyclass',
#  'device_type': 'cisco_ios',
#  'password': getpass
#}
#
#to send a command to the device:
#output = c.send_command("show ip int brief")
#
## net_connect.find_prompt()
#
## verify configuration changes function
#
## start the main program steps
#
## output progress of the main steps
#