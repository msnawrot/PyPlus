import xmltodict
from pprint import pprint

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


# Optional - create a second function that uses xmltodict to read and parse a
# filename that you pass in. This function should support a "force_list"
# argument that is passed to xmltodict.parse(). Reminder, the force_list
# argument of xmltodict takes a dictionary where the dictionary key-name is the
# XML element that is required to be a list.
# Use this new function to parse the "show_security_zones_single_trust.xml".
# Verify the Python data type is now a list for the
# ['zones-information']['zones-security'] element.

def second_function(filename):
    result = xmltodict.parse(filename, force_list={"zones-security": True})
    return result

print()
print()
# print(type(second_function(zones_xml['zones-information']['zones-security'])))
second_answer = second_function(zone_xml)
pprint(type(second_answer['zones-information']['zones-security']))
