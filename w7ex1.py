from lxml import etree

with open("show_security_zones.xml") as fr:
    file_content = fr.read()

parsed_xml = etree.fromstring(file_content)

print(parsed_xml)
print(type(parsed_xml))
