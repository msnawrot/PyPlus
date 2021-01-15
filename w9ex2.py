from my_devices import network_devices
from my_functions import open_napalm_connection, create_backup
from pprint import pprint

connections_list = []

for device in network_devices:
    conn = open_napalm_connection(device)
    connections_list.append(conn)

# 2b pprint the arp table for each device. gather the info with a napalm getter
for conn in connections_list:
    arp_table = conn.get_arp_table()
    print(conn.hostname, ":")
    pprint(arp_table)
    print("-" * 40)
    print()

# 2c attempt to use get_ntp_peers() method against both devices. gracefully handle exceptions
for conn in connections_list:
    try:
        ntp_peers = conn.get_ntp_peers()
        print(conn.hostname, ":")
        pprint(ntp_peers)
        print("-" * 40)
        print()
    except Exception as ex:
        print(ex)

# 2d create anothe func in my_functions.py, called create_backup.
for conn in connections_list:
    create_backup(conn)
