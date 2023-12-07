import yaml, json, requests

url = 'config.yaml'

def parse(file_path):
    with open(file_path, "r") as f:
        config = yaml.safe_load(f)
        
        return config


def healthCheck(config):
    
    for data in config:
        name = data.get('name')
        print(name)




if __name__ == "__main__":

    parser = parse(url)
    healthCheck(parser)
