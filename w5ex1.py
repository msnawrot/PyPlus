from jinja2 import Template

# bgp_config = """
# router bgp {{ local_as }}
#   neighbor {{ peer1_ip }} remote-as {{ peer1_as }}
#     update-source loopback99
#     ebgp-multihop 2
#     address-family ipv4 unicast
#   neighbor {{ peer2_ip }} remote-as {{ peer2_as }}
#     address-family ipv4 unicast
# """
bgp_config = """
router bgp {{ local_as }}
  {% for neighbor in neighbors %}neighbor {{ neighbor["peer_ip"] }} remote-as {{ neighbor["peer_as"] }}
  {% if neighbor["peer_ip"] == "10.1.20.2" %}update-source loopback99
  ebgp-multihop 2 {% endif %}
  address-family ipv4 unicast
  {% endfor %}
"""
my_dict = {
    "local_as": 10,
    "neighbors": [{
        "peer_ip": "10.1.20.2",
        "peer_as": 20}, {
        "peer_ip": "10.1.30.2",
        "peer_as": 30}]
}
j2_template = Template(bgp_config)
# output = j2_template.render(local_as=10, peer1_ip="10.1.20.2", peer1_as=20, peer2_ip="10.1.30.2", peer2_as=30)
output = j2_template.render(**my_dict)
print(output)
