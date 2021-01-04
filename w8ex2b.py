from jnpr_devices import srx2
from jnpr.junos import Device
from jnpr.junos.op.routes import RouteTable
from jnpr.junos.op.arp import ArpTable

def check_connected(device):
    try:
        if device.connected == True:
            return True
        else: return False
    except Exception as e:
        raise e

def gather_routes(device):
    temproutes = RouteTable(device)
    temproutes.get()
    return temproutes

def gather_arp_table(device):
    temparps = ArpTable(device)
    temparps.get()
    return temparps

def print_output(device, table1, table2):
    print("Hostname :", device['host'])
    print("NETCONF port :", device['port'])
    print("Username :", device['user'])
    print("Routing Table :\n", table1)
    print("ARP Table :\n", table2)

if __name__ == "__main__":
    # make a Device
    my_device = Device(**srx2)
    # connect to device
    my_device.open()
    # check_connected
    if check_connected(my_device) == True:
        # gather_routes
        routes = gather_routes(my_device)
        # gather_arp_table
        arps = gather_arp_table(my_device)

    if my_device and routes and arps:
        # print_output
        print_output(my_device, routes, arps)
    
