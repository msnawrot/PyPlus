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

# Compare the Python "type" of the elements at
# ['zones-information']['zones-security']. What is the difference between the
# two data types? Why?

if type(zones['zones-information']['zones-security']) == type(zone['zones-information']['zones-security']):
    print("Match")
else:
    print("No Match")
# zones returns a list, since multiple elements have the tag 'zones-security'
# zone returns an OrderedDict, since a single element has the tag 'zones-security'
print(type(zones['zones-information']['zones-security']))
print(type(zone['zones-information']['zones-security']))
