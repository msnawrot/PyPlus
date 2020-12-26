import xmltodict

with open("show_security_zones.xml") as f:
    zones_xml = f.read().strip()

with open("show_security_zones_single_trust.xml") as f:
    zone_xml = f.read().strip()

def generic(filename):
    temp1 = xmltodict.parse(filename)
    return temp1

zones = generic(zones_xml)
zone = generic(zone_xml)
print(zones)
print()
print(zone)
