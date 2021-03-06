from jnpr_devices import srx2
from jnpr.junos import Device
from jnpr.junos.op.routes import RouteTable
from jnpr.junos.op.arp import ArpTable
from w8ex2b import check_connected
from jnpr.junos.utils.config import Config
from jnpr.junos.exception import LockError

if __name__ == "__main__":
    # make a Device
    my_device = Device(**srx2)
    # connect to device
    my_device.open()
    # check_connected
    if check_connected(my_device) == True:
        cfg = Config(my_device)
        cfg.lock()
        cfg.load("set system host-name python4life")
        print(cfg.diff())
        cfg.rollback(0)
        print("-" * 20)
        print(cfg.diff())
