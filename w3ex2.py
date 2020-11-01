import yaml

wholelotta = [{
    'device_name': 'cisco4', # (Cisco IOS-XE)
    'host': 'cisco4.lasthop.io',
    'username': 'MrAnderson',
    'password': 'Neo123'
},
{
    'device_name': 'arista1', # (Arista vEOS switch)
    'host': 'arista1.lasthop.io',
    'username': 'MrAnderson',
    'password': 'Neo123'
},
{
    'device_name': 'arista2', # (Arista vEOS switch)
    'host': 'arista2.lasthop.io',
    'username': 'MrAnderson',
    'password': 'Neo123'
},
{
    'device_name': 'arista3', # (Arista vEOS switch)
    'host': 'arista3.lasthop.io',
    'username': 'MrAnderson',
    'password': 'Neo123'
},
{
    'device_name': 'arista4', # (Arista vEOS switch)
    'host': 'arista4.lasthop.io',
    'username': 'MrAnderson',
    'password': 'Neo123'
},
{
    'device_name': 'srx2', # (Juniper SRX)
    'host': 'srx2.lasthop.io',
    'username': 'MrAnderson',
    'password': 'Neo123'
},
{
    'device_name': 'nxos1', # (NX-OSv Switch)
    'host': 'nxos1.lasthop.io',
    'username': 'MrAnderson',
    'password': 'Neo123'
},
{
    'device_name': 'nxos2', # (NX-OSv Switch)
    'host': 'nxos2.lasthop.io',
    'username': 'MrAnderson',
    'password': 'Neo123'
}]

with open("my_devices.yml", 'w') as yf:
    yaml.dump(wholelotta, f, default_flow_style=False)
