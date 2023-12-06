import yaml, json, requests

url = 'config.yaml'

def parse(file_path):
    with open(file_path, "r") as f:
        config = yaml.safe_load(f)
        
        return config


def healthCheck(config):
    
    for data in config:
        print(json.dumps(data, indent=4))



parser = parse(url)
healthCheck(parser)
