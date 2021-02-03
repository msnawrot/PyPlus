from concurrent.futures import ProcessPoolExecutor
from w10my_devices import network_devices as devices
from datetime import datetime
from w10my_functions import ssh_command2

my_command = "show version"
start_time = datetime.now()

max_threads = 4

with ProcessPoolExecutor(max_threads) as pool:
    results_generator = pool.map(ssh_command2, my_command, devices)
    for result in results_generator:
        print("Result: " + result)

print("\nElapsed time: " + str(datetime.now() - start_time))
