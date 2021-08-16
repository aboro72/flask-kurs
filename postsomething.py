import requests
import json

url = "http://127.0.0.1:80/postme/"
data = {'data': 'mydata'}
result = requests.post(url, json.dumps(data))



