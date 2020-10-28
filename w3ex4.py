import json

with open("w3arp.json") as f:
    json_out = json.load(f)

arp_dict = dict()
arp_list = json_out['ipV4Neighbors']
for entry in arp_list:
    address = entry['address']
    mac = entry['hwAddress']
    arp_dict[address] = mac

print(arp_dict)

expected_output = {'172.17.17.1': 'dc38.e111.97cf', '172.17.16.1': '90e2.ba5c.25fd'}
print(arp_dict == expected_output)
