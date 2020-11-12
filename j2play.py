from jinja2 import Template

template = """
{%- for slot in range(1, 4) %}
  {%- for port_number in range(1, 25) %}
interface GigabitEthernet0/{{ slot }}/{{ port_number }}
  {%- endfor %}
  {#- this is a comment in Jinja2 #}
{%- endfor %}
"""

j2_template = Template(template)
output = j2_template.render()
print(output)
