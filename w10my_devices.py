from getpass import getpass
my_password = getpass()

cisco3 = {
    'hostname':"cisco3.lasthop.io",
    'device_type':"ios",
    'username':"pyclass",
    'password': my_password,
}

arista1 = {
    'hostname':"arista1.lasthop.io",
    'device_type':"eos",
    'username':"pyclass",
    'password': my_password,
    'global_delay_factgor': 4,
}

arista2 = {
    'hostname':"arista2.lasthop.io",
    'device_type':"eos",
    'username':"pyclass",
    'password': my_password,
    'global_delay_factgor': 4,
}

srx2 = {
    'hostname':"srx2.lasthop.io",
    'device_type':"junos",
    'username':"pyclass",
    'password': my_password,
}

network_devices = [cisco3, arista1, arista2, srx2]
