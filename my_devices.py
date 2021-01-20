from getpass import getpass
my_password = getpass()

cisco3 = {
    'hostname':"cisco3.lasthop.io",
    'device_type':"ios",
    'username':"pyclass",
    'password': my_password,
    'optional_args':{},
}

arista1 = {
    'hostname':"arista1.lasthop.io",
    'device_type':"eos",
    'username':"pyclass",
    'password': my_password,
    'optional_args':{},
}

# network_devices = [cisco3, arista1]

# 4a - add nxos1 to this file.

nxos1 = {
    'hostname':"nxos1.lasthop.io",
    'device_type':"nxos",
    'username':"pyclass",
    'password': my_password,
    'optional_args':{"port": 8443},
}

network_devices = [cisco3, arista1, nxos1]
