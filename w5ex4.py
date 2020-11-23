from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment

# load jinja2 Environment
env = Environment(undefined=StrictUndefined)
env.loader = FileSystemLoader(['.','./jinja2'])

# j2_vars defined
j2_vars = {
}

vrfs = [{'vrf_name': 'red',
        'rd_number': '100:1',
        'ipv4_true': True,
        'ipv6_true': True},
        {'vrf_name': 'orange',
        'rd_number': '101:1',
        'ipv4_true': True,
        'ipv6_true': True},
        {'vrf_name': 'yellow',
        'rd_number': '102:1',
        'ipv4_true': True,
        'ipv6_true': True},
        {'vrf_name': 'green',
        'rd_number': '103:1',
        'ipv4_true': True,
        'ipv6_true': True},
        {'vrf_name': 'blue',
        'rd_number': '104:1',
        'ipv4_true': True,
        'ipv6_true': True}
        ]
# jinja2 templates
j2_template = "w5ex4_tpl.j2"
template = env.get_template(j2_template)

for vrf in vrfs:
    rendered = template.render(**vrf)
    print(rendered)
