from netmiko import ConnectHandler
from w10my_devices import network_devices as devices
from datetime import datetime

def show_command(command, **device):
    connection = ConnectHandler(**device)
    output = connection.send_command(command)
    connection.disconnect()
    return output

my_command = "show version"
start_time = datetime.now()

for device in devices:
    print("=" * 40)
    print("Device: " + device['host'])
    print(show_command(my_command, **device))
    print("+" * 40)

print("Elapsed time: " + datetime.now() - str(start_time))
