import xmltodict

# Using xmltodict, load the show_security_zones.xml file as a Python dictionary.
# Print out this new variable and its type. Note, the newly created object is an
# OrderedDict; not a traditional dictionary

xmlfile = open("show_security_zones.xml")
xmldata = xmlfile.read().strip()
my_xml = xmltodict.parse(xmldata)
print(my_xml)
print(type(my_xml))

# Print the names and an index number of each security zone in the XML data
# from Exercise 2a. Your output should look similar to the following (tip,
# enumerate will probably help):
# Security Zone #1: trust
# Security Zone #2: untrust
# Security Zone #3: junos-host

for count, value in enumerate(my_xml['zones-information']['zones-security']):
    print("Security Zone #%s: %s" % (count + 1, value['zones-security-zonename']))
    # print("Security Zone #{}: {}".format(count + 1, value['zones-security-zonename']))
