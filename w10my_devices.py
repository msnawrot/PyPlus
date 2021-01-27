from getpass import getpass
my_password = getpass()

cisco3 = {
    'host':"cisco3.lasthop.io",
    'device_type':"cisco_ios",
    'username':"pyclass",
    'password': my_password,
}

arista1 = {
    'host':"arista1.lasthop.io",
    'device_type':"arista_eos",
    'username':"pyclass",
    'password': my_password,
    'global_delay_factgor': 4,
}

arista2 = {
    'host':"arista2.lasthop.io",
    'device_type':"arista_eos",
    'username':"pyclass",
    'password': my_password,
    'global_delay_factgor': 4,
}

srx2 = {
    'host':"srx2.lasthop.io",
    'device_type':"juniper_junos",
    'username':"pyclass",
    'password': my_password,
}

network_devices = [cisco3, arista1, arista2, srx2]
