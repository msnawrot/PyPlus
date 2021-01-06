from jnpr_devices import srx2
from w8ex2b import check_connected, gather_routes

# make a Device
my_device = Device(**srx2)
# connect to device
my_device.open()
# check_connected
if check_connected(my_device) == True:
    # gather_routes
    routes = gather_routes(my_device)
