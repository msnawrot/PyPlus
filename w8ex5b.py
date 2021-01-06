from jnpr.junos import Device
from lxml import etree
from w8ex2b import srx2
from pprint import pprint

my_device = Device(**srx2)
my_device.open()
xml_out = my_device.rpc.get_interface_information()
print(etree.tostring(xml_out, encoding="unicode"))
