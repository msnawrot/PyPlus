from my_devices import network_devices
from getpass import getpass
from napalm import get_network_driver
from pprint import pprint

def open_napalm_connection(obj_dict):
    # create a duplicate of the obj_dict so that the original isn't modified
    device = obj_dict.copy()
    # pop a platform as this is an invalid kwarg to NAPALM
    platform = device.pop("device_type")
    driver = get_network_driver(platform)
    conn = driver(**device)
    conn.open()
    return conn


if __name__ == "__main__":
    connections = []
    for device in network_devices:
        conn = open_napalm_connection(device)
        connections.append(conn)

    for obj in connections:
        print()
        print(obj)
        print()
        print("Facts about", obj.platform)
        pprint(obj.get_facts())
        obj.close()
