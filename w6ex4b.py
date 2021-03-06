import yaml
import pyeapi
from getpass import getpass
from jinja2 import Template

template = "no interface {{ intf_name }}"

def read_yaml(filename):
    with open(filename) as f:
        yaml_out = yaml.load(f, Loader=yaml.FullLoader)
    return yaml_out


devices = read_yaml('w6ex4.yml')
passwd = getpass("Password: ")
# loop interates over each switch
# within the loop, first a jinja2 template is rendered,
# second, the config is pushed to the switch
# foobar needs to be the data dictionary
for switch in devices:
    for key, eapi_stuff in switch.items():
        j2_template = Template(template)
        cfg = j2_template.render(**eapi_stuff['data'])
        cfg = cfg.splitlines()
        connection = pyeapi.client.connect(password=passwd,**eapi_stuff)
        device = pyeapi.client.Node(connection)
        output = device.config(cfg)
