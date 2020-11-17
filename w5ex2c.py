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
filename = "w5ex2c.yml"
with open(filename) as f:
    yaml_out = yaml.load(f, Loader=yaml.FullLoader)

global_password = getpass("Router password, please: ")

# jinja2 environment
env = Environment(undefined=StrictUndefined)
env.loader = FileSystemLoader([".", "./jinja2"])

# jinja2 templates
j2_template = "w5ex2c_tpl.j2"

def render_config(routers):
    for e in routers:
        j2_vars = e[0]['j2_vars']
        #print(type(j2_vars))
        #print(j2_vars)
        template = env.get_template(j2_template)
        output = template.render(**j2_vars)
        print(f"rendered config for {j2_vars['host']}:\n", output)
        print()
        print("Storing rendered config...")
        e[1]['nm_vars'].update({'config': output})
        print()

render_config(yaml_out)


## push configuration changes function
## router must be a dictionary, with session_log, host, username, password, and device_type keys
## why not have a config key in the dictionary, too

def find_prompt(routers):
    for e in routers:
        nm_vars = e[1]['nm_vars']
        config = nm_vars.pop('config')
        nm_vars.update({'password': global_password})
        net_connect = ConnectHandler(**nm_vars)
        output = net_connect.find_prompt()
        # output = net_connect.send_config_set(config)
        print(output)

def push_config_list(routers):
    for e in routers:
        print("Preparing for config push...\n")
        nm_vars = e[1]['nm_vars']
        rawconfig = nm_vars.pop('config')
        config_list = rawconfig.split('\n')
        nm_vars.update({'password': global_password})
        net_connect = ConnectHandler(**nm_vars)
        print(f"Config push to {nm_vars['host']}...\n")
        output = net_connect.send_config_set(config_list)
        if output:
            print(f"Config pushed successfully.  Check {nm_vars['session_log']} for details.\n")

push_config_list(yaml_out)

## verify configuration changes function
# verify you are able to ping between the devices and also

for router in yaml_out:
    j2_vars, nm_vars = router
    j2_vars = j2_vars['j2_vars']
    nm_vars = nm_vars['nm_vars']
    nm_vars.update({'password': global_password})
    net_connect = ConnectHandler(**nm_vars, session_log_file_mode="append")
    output = net_connect.send_command(f"ping {j2_vars['peer_ip']}")
    print(output)
# no textfsm for ping, so I'll have to write code to parse the output myself
# would like a boolean that represents "can ping successfully"
# for now, just print ping output to screen for the engineer to verify

# verify that the BGP session reaches the established state.
# textfsm has a template for cisco_nxos_show_ip_bgp, neighbors, summary
    output = net_connect.send_command("show ip bgp neighbors", use_textfsm=True)
    print(output)
## start the main program steps
#
## output progress of the main steps
#

#to send a command to the device:
#output = c.send_command("show ip int brief")
#
## net_connect.find_prompt()
#
