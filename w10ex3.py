from concurrent.futures import ThreadPoolExecutor
from w10my_devices import network_devices as devices
from datetime import datetime
from w10my_functions import ssh_command2

my_command = "show version"
start_time = datetime.now()

max_threads = 4
pool = ThreadPoolExecutor(max_threads)

futures = []
for device in devices:
    future = pool.submit(ssh_command2, my_command, device)
    futures.append(future)

wait(futures)

for future in futures:
    print("Result: " + future.result())

print("\nElapsed time: " + str(datetime.now() - start_time))
