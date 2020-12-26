from lxml import etree

with open("show_security_zones.xml") as fr:
    file_content = fr.read()

parsed_xml = etree.fromstring(file_content)

print(parsed_xml)
print(type(parsed_xml))
#  Using your XML variable from exercise 1a, print out the entire XML tree in a
# readable format (ensure that the output string is a unicode string).
readable = etree.tostring(parsed_xml).decode()
print(readable)
