from ciscoconfparse import CiscoConfParse

BGPconfig = """
router bgp 44
 bgp router-id 10.220.88.38
 address-family ipv4 unicast
 !
 neighbor 10.220.88.20
  remote-as 42
  description pynet-rtr1
  address-family ipv4 unicast
   route-policy ALLOW in
   route-policy ALLOW out
  !
 !
 neighbor 10.220.88.32
  remote-as 43
  address-family ipv4 unicast
   route-policy ALLOW in
   route-policy ALLOW out
"""

cisco_obj = CiscoConfParse(BGPconfig.splitlines())
neighbors = list()
BGPpeers = list()
conf_nei = cisco_obj.find_objects(r"neighbor")
for nei in conf_nei:
    _, x = nei.text.split()
    _, y = nei.children[0].text.split()
    BGPpeers.append((x, y))
print("BGP Peers:")
print(BGPpeers)

# documenting Kirk's solution, because I think it is more elegant than mine
# also, my script would hit on OSPF, EIGRP neighbors, not just BGP neighbors
#neighbors = cisco_obj.find_objects_w_parents(
#    parentspec=r"router bgp", childspec=r"neighbor"
#)
#for neighbor in neighbors:
#    _, neighbor_ip = neighbor.text.split()
#    for child in neighbor.children:
#        if "remote-as" in child.text:
#            _, remote_as = child.text.split()
#    bgp_peers.append((neighbor_ip, remote_as))
