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
    'hostname':"cisco3.lasthop.io",
    'device_type':"eos",
    'username':"pyclass",
    'password': my_password,
    'optional_args':{},
}
