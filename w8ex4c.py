from jnpr_devices import srx2
from w8ex2b import check_connected, gather_routes
from jnpr.junos.utils.config import Config
from jnpr.junos import Device

# make a Device
my_device = Device(**srx2)
# connect to device
my_device.open()
# check_connected
if check_connected(my_device) == True:
    print("Connection established")
    # gather_routes
    pre_routes = gather_routes(my_device)
    print("gathered pre-change route table")
    # stage a config from a file
    cfg = Config(my_device)
    cfg.lock()
    print("config locked")
    cfg.load(path="conf.txt", format="text", merge=True)
    print(cfg.diff())
