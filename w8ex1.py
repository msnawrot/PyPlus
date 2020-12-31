from jnpr.junos import Device
from getpass import getpass
from pprint import pprint

my_device = Device(
    host="srx2.lasthop.io",
    password=getpass(),
    user="pyclass",
)

my_device.open()
pprint(my_device.facts)
