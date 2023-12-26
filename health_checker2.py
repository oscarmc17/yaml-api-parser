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
        headers = data.get('headers', {})
        body = data.get('body')
    
        # print(f"{name}, {url}, {method}, {header}, {body}\n")

        try:
            # response = requests.request(method, url, headers=headers, json=body, timeout=5)
            response = requests.get(url, headers=headers, json=body, timeout=5)
            status_code = response.status_code
            print(status_code)
        except e as e:
            print(e)
            
        




if __name__ == "__main__":

    parser = parse(url)
    healthCheck(parser)
