import os.path
from napalm import get_network_driver

def open_napalm_connection(obj_dict):
    # create a duplicate of the obj_dict so that the original isn't modified
    device = obj_dict.copy()
    # pop a platform as this is an invalid kwarg to NAPALM
    platform = device.pop("device_type")
    driver = get_network_driver(platform)
    conn = driver(**device)
    conn.open()
    return conn

def create_backup(conn_obj):
    config_dict = conn_obj.get_config("running")
    hostname = str(conn_obj.hostname)
    filename = hostname + ".txt"
    cfg_str = config_dict['running']
    with open(filename, "w") as fw:
        fw.write(cfg_str)
    if os.path.exists(filename):
        print("The config for {} was backed up successfully in {}.".format(hostname, filename))
    else:
        print("Backup failed for {}.".format(hostname))

def create_checkpoint(conn_obj):
    checkpoint = conn_obj._get_checkpoint_file()
    hostname = str(conn_obj.hostname)
    filename = hostname + "-checkpoint.txt"
    with open(filename, "w") as fw:
        fw.write(checkpoint)
