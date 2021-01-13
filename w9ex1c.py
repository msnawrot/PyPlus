from my_devices.py import cisco3, arista1
from getpass import getpass
from napalm import get_network_driver

def create_connection(obj_dict):
    # create a duplicate of the obj_dict so that the original isn't modified
    device = obj_dict.copy()
    # pop a platform as this is an invalid kwarg to NAPALM
    platform = device.pop("device_type")
    driver = get_network_driver(platform)
    conn = driver(**device)
    conn.open()
    return conn


if "__name__" == "__main__":
    connections = []
    connections.append(create_connection(cisco3))
    connections.append(create_connection(arista1))
