from Netmiko import ConnectHandler
from w10my_devices import network_devices as devices
from datetime import datetime

def show_command(**device, command):
    connection = ConnectHandler(**device)
    output = connection.send_command(command)
    connection.disconnect()
    return output

my_command = "show version"
start_time = datetime.now()

for device in devices:
    print("=" * 40)
    print("Device: " + device['hostname'])
    print(show_command(device, my_command))
    print("+" * 40)

print("Elapsed time: " + datetime.now() - str(start_time))
