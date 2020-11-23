from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment

# load jinja2 Environment
env = Environment(undefined=StrictUndefined)
env.loader = FileSystemLoader(['.','./jinja2'])

# j2_vars defined
j2_vars = {
        'vrf_name': 'blue',
        'rd_number': '100:1',
        'ipv4_true': True,
        'ipv6_true': True
}
# jinja2 templates
j2_template = "w5ex3_tpl.j2"

template = env.get_template(j2_template)
rendered = template.render(**j2_vars)
print(rendered)
