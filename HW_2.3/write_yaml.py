import yaml

with open('data.yml', 'w') as text:
    data = {
        'name': 'банан',
        'price': 30
    }
    yaml.dump(data, text, allow_unicode=True, default_flow_style=False)