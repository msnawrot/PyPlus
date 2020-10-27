import yaml
from pprint import pprint

filename = input("Enter filename: ")
with open(filename) as f:
    yaml_out = yaml.load(f, Loader=yaml.FullLoader)
pprint(yaml_out)
