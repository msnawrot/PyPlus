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
    # fix the append to match only the IP address, not "neighbor "
    x = nei.text
    y = nei.children[0].text
    temp_tuple = (x, y)
    BGPpeers.append(temp_tuple)
print(BGPpeers)
