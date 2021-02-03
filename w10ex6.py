from concurrent.futures import ProcessPoolExecutor, as_completed
from w10my_devices import network_devices as devices
from datetime import datetime
from netmiko import ConnectHandler

# defining ssh_command2 here b/c the version in w10my_functinos has opposite order of arguments
def ssh_command2(device, command):
    connection = ConnectHandler(**device)
    output = connection.send_command(command)
    connection.disconnect()
    return output

start_time = datetime.now()
max_procs = 4

with ProcessPoolExecutor(max_procs) as pool:
    cmd_list = ["show ip arp"]
    results_generator = pool.map(ssh_command2, devices, cmd_list)
    for result in results_generator:
        print("Result: " + result)

print("\nElapsed time: " + str(datetime.now() - start_time))
