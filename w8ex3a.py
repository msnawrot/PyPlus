from jnpr_devices import srx2
from jnpr.junos import Device
from jnpr.junos.op.routes import RouteTable
from jnpr.junos.op.arp import ArpTable
import w8ex2b
from jnpr.junos.utils.config import Config

if __name__ == "__main__":
    # make a Device
    my_device = Device(**srx2)
    # connect to device
    my_device.open()
    # check_connected
    if check_connected(my_device) == True:
        cfg = Config(my_device)
        cfg.lock()
    try:
        cfg.lock()
    except LockError as e:
        raise e
