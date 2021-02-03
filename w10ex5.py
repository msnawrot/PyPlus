from concurrent.futures import ProcessPoolExecutor, as_completed
from w10my_devices import network_devices as devices
from datetime import datetime
from w10my_functions import ssh_command2

my_command = "show version"
start_time = datetime.now()

max_threads = 4

with ProcessPoolExecutor(max_threads) as pool:

    futures = []
    for device in devices:
        future = pool.submit(ssh_command2, my_command, device)
        futures.append(future)
    
    for future in as_completed(futures):
        print("Result: " + future.result())

print("\nElapsed time: " + str(datetime.now() - start_time))
