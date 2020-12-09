from my_funcs import read_yaml
from my_funcs import run_show_command
from getpass import getpass

device_dict = read_yaml('w6ex2a.yml')
device_dict['password'] = getpass("password please: ")
show_cmd = "show ip route"
result = run_show_command(show_cmd,**device_dict)
# LOL look how long this is!!!
# print(result[0]['result']['vrfs']['default']['routes']['10.220.88.0/24']['vias'][0]['interface'])
# Vlan1

for k, v in result[0]['result']['vrfs']['default']['routes'].items():
    print("\n" + k, "\t", v['routeType'], end = '')
    if v['routeType'] == "static":
        for i in v['vias']:
            print("\t" +i['nexthopAddr'])
