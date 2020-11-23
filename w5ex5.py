from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment

# load jinja2 Environment
env = Environment(undefined=StrictUndefined)
env.loader = FileSystemLoader(['.','./jinja2'])

# j2_vars defined
j2_vars = {
        'ntp_servers': ['130.126.24.24', '152.2.21.1'],
        'timezone': 'PST',
        'timezone_offset': '-8 0',
        'timezone_dst': 'PDT'
}


# jinja2 templates
j2_template = "w5ex5showrun.j2"
template = env.get_template(j2_template)
rendered = template.render(**j2_vars)
print(rendered)
