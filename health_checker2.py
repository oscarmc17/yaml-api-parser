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
            response_code = response.status_code
            latency = response.elapsed.total_seconds() * 1000
            # print(latency)

            if response_code <= 299 and latency < 500:
                result = 'UP'
            else:
                result = 'DOWN'
            
            print(f"Endpoint {name} has HTTP response code: {response_code} and response latency: {latency}")

            # if 200 <= response_code < 300 and latency < 500:
            #     result = "UP"
            # else:
            #     result = "DOWN"

            # print(result)


        except e as e:
            print(e)
            
        




if __name__ == "__main__":

    parser = parse(url)
    healthCheck(parser)
