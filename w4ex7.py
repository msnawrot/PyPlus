import textfsm
from pprint import pprint

template_file = "w4ex2.template"
template = open(template_file)

with open("w4ex1.txt") as f:
    raw_text_data = f.read()

re_table = textfsm.TextFSM(template)
data = re_table.ParseText(raw_text_data)

int_list = list()
for entry in data:
    loop_dict = {
    'DUPLEX' : entry[3],
    'PORT_NAME' : entry[0],
    'PORT_TYPE' : entry[5],
    'SPEED' : entry[4],
    'STATUS' : entry[1],
    'VLAN' : entry[2]}
    int_list.append(loop.dict)

pprint(int_list)
