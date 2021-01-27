import threading
from w10my_devices import network_devices as devices
from datetime import datetime

my_command = "show version"
start_time = datetime.now()

for device in devices:
    my_thread = threading.Thread(target=ssh_command, args=(device,))
    my_thread.start()

main_thread = threading.currentThread()
for some_thread in threading.enumerate():
    if some_thread != main_thread:
        print(some_thread)
        some_thread.join()

print("\nElapsed time: " + str(datetime.now() - start_time))
