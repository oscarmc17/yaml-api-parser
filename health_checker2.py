import yaml, json, requests

url = 'config.yaml'

def parse(file_path):
    with open(file_path, "r") as f:
        config = yaml.safe_load(f)
        
        return config


def healthCheck(config):
    
    for data in config:
        name = data.get('name')
        url = data.get('url')
        method = data.get('method', 'GET')
        header = data.get('headers', {})
        body = data.get('body')




if __name__ == "__main__":

    parser = parse(url)
    healthCheck(parser)
