from lxml import etree

with open("show_security_zones.xml") as f:
    zones_xml = f.read().strip()

my_xml = etree.fromstring(zones_xml)
# use .find() method to retreive the first "zones-security" element.
# result = my_xml.find("zones-security")

# print("Find tag of the first zones-security element")
# print("-" * 15)
# print(result.tag)
# print()
# print("Find tag of all child elements of the first", result.tag, "element")
# print("-" * 15)
# for child in result.getchildren():
#     print(child.tag)

# Use the find() method to find the first "zones-security-zonename". Print out
# the zone name for that element (the "text" of that element).
# result = my_xml[0].find("zones-security-zonename")
# print()
# print("The text of the first \"zones-security-zonename\" is :", result.text)
# print()

# Use the findall() method to find all occurrences of "zones-security". For
# each of these security zones, print out the security zone name
# ("zones-security-zonename", the text of that element).

results = my_xml.findall("zones-security")

print()
print("The zones' names in this xml are:")
for result in results:
    zonename = result.find("zones-security-zonename")
    print(zonename.text)
