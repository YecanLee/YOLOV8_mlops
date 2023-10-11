import time
import requests
url = 'https://us-central1-dtumlops-335110.cloudfunctions.net/function-2'
payload = {'message': 'Hello, General Kenobi'}

for _ in range(1000):
    r = requests.get(url, params=payload)
