from my_devices import network_devices
from my_functions import open_napalm_connection, create_backup
from pprint import pprint

connections_list = []

for device in network_devices:
    conn = open_napalm_connection(device)
    connections_list.append(conn)

# 3b create two text files, one per device.  in each, create loopbacks.
# 3b for both devices, use load_merge_candidate() method to stage candidate config.
# 3b use compare_config() method to print out differences.

for conn in connections_list:
    print(f"Loading candidate config for {conn.hostname}.")
    filename = f"{conn.hostname}-loopbacks.txt"
    conn.load_merge_candidate(filename=filename)
    print()

# 3c commit the pending changes to each device, and check the diff once again.
for conn in connections_list:
    print(f"Comparing config for {conn.hostname}.")
    print(conn.compare_config())
    print()
    my_answer = input("Press Y/y to push the above config. Press N/n to not.")
    if my_answer.lower() = "y":
        conn.commit_config()
        print("Configuration pushed")
        print()
        print("Below is another config diff, and it should be identical.")
        print(conn.compare_config())
    elif my_answer.lower() = "n":
        print("Config not committed.")
    else:
        my_answer = input(
            '...only Y/y or N/n are acceptable answers. To quote BGO, "We\'re done here."'
        )
