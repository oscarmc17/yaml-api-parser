import yaml, json, requests, time

url = 'config.yaml'

def parse(file_path):
    with open(file_path, "r") as f:
        config = yaml.safe_load(f)
        
        return config


def healthCheck(config):
    
    availability = {}

    while True:
        for data in config:
            name = data.get('name')
            url = data.get('url')
            method = data.get('method', 'GET')
            headers = data.get('headers', {})
            body = data.get('body')
        
            # print(f"{name}, {url}, {method}, {header}, {body}\n")

            try:
                response = requests.get(url, headers=headers, json=body, timeout=5)
                response_code = response.status_code
                latency = response.elapsed.total_seconds() * 1000
                # print(latency)

                if response_code <= 299 and latency < 500:
                    result = 'UP'
                else:
                    result = 'DOWN'
                
                print(f"Endpoint '{name}' is {result}. Response Code: {response_code}. Latency: {latency} ms.")

                # Update availability dictionary
                if url not in availability:
                    availability[url] = {'total': 1, 'up': 1 if result == 'UP' else 0}
                else:
                    availability[url]['total'] += 1
                    availability[url]['up'] += 1 if result == 'UP' else 0

            except e as e:
                print(e)

        time.sleep(2)
        
        for url, stats in availability.items():
            availability_percentage = round((stats['up'] / stats['total']) * 100)
            print(f"{url} has {availability_percentage}% availability percentage")


    # print(json.dumps(availability, indent=2))
        




if __name__ == "__main__":

    parser = parse(url)
    healthCheck(parser)
