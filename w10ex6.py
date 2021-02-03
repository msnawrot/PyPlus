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

my_command = "show version"
start_time = datetime.now()

max_threads = 4

with ProcessPoolExecutor(max_threads) as pool:
    results_generator = pool.map(ssh_command2, devices, my_command)
    for result in results_generator:
        print("Result: " + result)

print("\nElapsed time: " + str(datetime.now() - start_time))
