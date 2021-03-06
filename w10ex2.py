import threading
from w10my_devices import network_devices as devices
from datetime import datetime
from w10my_functions import ssh_command

my_command = "show version"
start_time = datetime.now()

for device in devices:
    my_thread = threading.Thread(target=ssh_command, args=(my_command, device))
    my_thread.start()

main_thread = threading.currentThread()
for some_thread in threading.enumerate():
    if some_thread != main_thread:
        print(some_thread)
        some_thread.join()

print("\nElapsed time: " + str(datetime.now() - start_time))
