from lxml import etree

with open("show_security_zones.xml") as fr:
    file_content = fr.read()

xml_obj = etree.fromstring(file_content)

print(xml_obj)
print(type(xml_obj))
#  Using your XML variable from exercise 1a, print out the entire XML tree in a
# readable format (ensure that the output string is a unicode string).
readable = etree.tostring(xml_obj).decode()
print(readable)

# Print out the root element tag name (this tag should have a value of
# "zones-information"). Print the number of child elements of the root element
# (you can retrieve this using the len() function).
print(xml_obj.tag)
print(len(xml_obj.getchildren()))

# Using both direct indices and the getchildren() method, obtain the first
# child element and print its tag name.
print()
print(xml_obj[0].tag)
print()
print(xml_obj.getchildren()[0].tag)
