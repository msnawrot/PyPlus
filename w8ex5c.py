from jnpr.junos import Device
from lxml import etree
from w8ex2b import srx2
from pprint import pprint

my_device = Device(**srx2)
my_device.open()
xml_out = my_device.rpc.get_interface_information(terse=True, normalize=True, interface_name="fe-0/0/7")
pprint(etree.tostring(xml_out, encoding="unicode", pretty_print=True))
