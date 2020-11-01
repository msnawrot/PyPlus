from pprint import pprint


arp_data = """
Protocol  Address          Age (min)  Hardware Addr   Type   Interface
Internet  10.220.88.1            67   0062.ec29.70fe  ARPA   GigabitEthernet0/0/0
Internet  10.220.88.20           29   c89c.1dea.0eb6  ARPA   GigabitEthernet0/0/0
Internet  10.220.88.22            -   a093.5141.b780  ARPA   GigabitEthernet0/0/0
Internet  10.220.88.37          104   0001.00ff.0001  ARPA   GigabitEthernet0/0/0
Internet  10.220.88.38          161   0002.00ff.0001  ARPA   GigabitEthernet0/0/0
"""

arp_list = arp_data.splitlines()
new_structure = []
for line in arp_list[1:]:
    _, ip_addr, _, hw_addr, _, intfc = line.split()
    new_structure.append({"ip address": ip_addr, "hw address": hw_addr, "interface": intfc})

pprint(new_structure)
