from lxml import etree

with open("show_version.xml", "rb") as f:
    xml_string = f.read().strip()

my_xml = etree.fromstring(xml_string)

print("The following line prints the namespace map.")
print(my_xml.nsmap)
print()
print("I like the output better in multiple lines, and the result of .nsmap is a dict")
for k, v in my_xml.nsmap.items():
    print(k, v)

#  use the find() method to access the text of the "proc_board_id" element
# (serial number).
print()
result = my_xml.find(".//{*}proc_board_id")
print("The serial number is:", result.text)
# for some reason .find("{*}proc_board_id") didn't work, and I needed the .//
