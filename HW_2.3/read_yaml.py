import yaml
from pprint import pprint

with open('GodFather.yml') as text:
    movie = yaml.load(text)
    pprint(movie)