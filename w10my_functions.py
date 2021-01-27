from netmiko import ConnectHandler

def ssh_command(command, device):
    print("=" * 40)
    print("Device: " + device['host'])
    connection = ConnectHandler(**device)
    output = connection.send_command(command)
    print(output)
    print("+" * 40)
    connection.disconnect()
    return output

def ssh_command2(command, device):
    connection = ConnectHandler(**device)
    output = connection.send_command(command)
    connection.disconnect()
    return output
