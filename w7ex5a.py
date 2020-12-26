from lxml import etree

with open("show_version.xml", "rb") as f:
    xml_string = f.read().strip()

my_xml = etree.fromstring(xml_string)

print(my_xml.nsmap)

# I like the output better in multiple lines, and the result of .nsmap is a dict
for k, v in my_xml.nsmap.items():
    print(k, v)
