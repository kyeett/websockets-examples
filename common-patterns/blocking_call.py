import requests

resp = requests.get('http://localhost:8500/v1/catalog/services')
print(resp.json())

headers = {'index': resp.headers['X-Consul-Index']}

resp = requests.get('http://localhost:8500/v1/catalog/services', params=headers)
print(resp.json())
