from jnpr_devices import srx2
from w8ex2b import check_connected, gather_routes
from jnpr.junos.utils.config import Config
from jnpr.junos import Device

def non_match_elements(list_a, list_b):
    non_match = []
    for i in list_a:
        if i not in list_b:
            non_match.append(i)
    return non_match


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
    print("config loaded")
    cfg.commit()
    print("config committed")
    cfg.unlock()
    post_routes = gather_routes(my_device)
    pre_routes = pre_routes.keys()
    post_routes = post_routes.keys()
    non_match = non_match_elements(post_routes, pre_routes)
    print("New routes: ", non_match)
