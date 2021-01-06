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
    cfg = Config(my_device)
    cfg.lock()
    print("config is locked")
    cfg.load("delete routing-options static route 203.0.113.1/32", format="set", merge=True)
    cfg.load("delete routing-options static route 203.0.113.15/32", format="set", merge=True)
    print("config is loaded")
    input("Press enter to commit..., ctrl-c to abort")
    cfg.commit()
    cfg.unlock()
    print("config committed")
    
