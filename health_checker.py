# import yaml
# import requests
# import time
# import signal
# import sys, json

# # Function to parse the YAML configuration file
# def parse_config(file_path):
#     with open(file_path, 'r') as file:
#         config = yaml.safe_load(file)
#     return config

# # Function to perform health checks on HTTP endpoints
# def health_check(config):
#     availability = {}  # Dictionary to store availability percentage for each domain
#     try:
#         while True:
#             for endpoint in config:
#                 name = endpoint.get('name')
#                 url = endpoint.get('url')
#                 method = endpoint.get('method', 'GET')
#                 headers = endpoint.get('headers', {})
#                 body = endpoint.get('body', None)

#                 try:
#                     response = requests.request(method, url, headers=headers, json=body, timeout=5)
#                     response_code = response.status_code
#                     latency = response.elapsed.total_seconds() * 1000  # Convert to milliseconds

#                     if 200 <= response_code < 300 and latency < 500:
#                         result = "UP"
#                     else:
#                         result = "DOWN"

#                     print(f"Endpoint '{name}' is {result} - Response Code: {response_code}, Latency: {latency} ms")

#                     # Update availability dictionary
#                     if url not in availability:
#                         availability[url] = {'total': 1, 'up': 1 if result == 'UP' else 0}
#                     else:
#                         availability[url]['total'] += 1
#                         availability[url]['up'] += 1 if result == 'UP' else 0

#                 except requests.RequestException as e:
#                     print(f"Error in making request to '{name}': {e}")

#             time.sleep(15)  # Wait for 15 seconds between health checks

#             # Calculate and log availability percentages
#             for url, stats in availability.items():
#                 availability_percentage = round((stats['up'] / stats['total']) * 100)
#                 print(f"{url} has {availability_percentage}% availability percentage")

#     except KeyboardInterrupt:
#         print("\nProgram terminated by user.")
#         sys.exit(0)

# if __name__ == "__main__":
#     if len(sys.argv) != 2:
#         print("Usage: python program.py <config_file_path>")
#         sys.exit(1)

#     config_file_path = sys.argv[1]
#     config = parse_config(config_file_path)
#     health_check(config)