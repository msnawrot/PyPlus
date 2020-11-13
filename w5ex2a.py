from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment

env = Environment(undefined=StrictUndefined)
env.loader = FileSystemLoader([".", "./jinja2"])

nxos1 = {"interface": "Ethernet1/1", "ip_addr": "10.1.100.1", "netmask": "24"}
nxos2 = {"interface": "Ethernet1/1", "ip_addr": "10.1.100.2", "netmask": "24"}

j2_template = "w5ex2a_tpl.j2"

for j2_vars in (nxos1, nxos2):
    template = env.get_template(j2_template)
    output = template.render(**j2_vars)
    print(output)
