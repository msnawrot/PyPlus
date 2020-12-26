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
print(xml_obj[0].tag)
print(xml_obj.getchildren()[0].tag)

# Create a variable named "trust_zone". Assign this variable to be the first
# "zones-security" element in the XML tree. Access this newly created variable
# and print out the text of the "zones-security-zonename" child
trust_zone = xml_obj[0]
print(trust_zone[0].text)

# Iterate through all of the child elements of the "trust_zone" variable. Print
# out the tag name for each child element.
print()
for child in trust_zone:
    print(child.tag) 
