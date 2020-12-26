
# Create an nxapi_plumbing "Device" object for nxos1
device = Device(
    api_format= "jsonrpc",
    transport= "https",
    port=8443,
    host='nxos1.lasthop.io',
    verify=False,
    username='pyclass',
    password=getpass()
)

# Send the "show interface Ethernet1/1" command to the device
raw_output = device.show("show interface Ethernet1/1")
# parse the output
print(raw_output)
# print out the following information:
