import yaml
import pyeapi
from getpass import getpass

def read_yaml(filename):
    with open(filename) as f:
        yaml_out = yaml.load(f, Loader=yaml.FullLoader)
    return yaml_out

def run_show_command(cmd, **device):
    connection = pyeapi.client.connect(**device)
    device = pyeapi.client.Node(connection)
    output = device.enable(cmd)
    # convert output to a list of tuples
    ip_mac_list = list()
    for addr_dict in output[0]['result']['ipV4Neighbors']:
        ip_addr = addr_dict['address']
        mac_addr = addr_dict['hwAddress']
        ip_mac_list.append((ip_addr, mac_addr))
    # print the list of tuples with a for loop
    print("IP Address\t MAC Address")
    for ip_addr, mac_addr in ip_mac_list:
        print(ip_addr, "\t", mac_addr)

if __name__ == "__main__":
    device_dict = read_yaml('w6ex2a.yml')
    device_dict['password'] = getpass("password please: ")
    show_cmd = "show ip arp"
    run_show_command(show_cmd, **device_dict)
