import requests
import json


url = 'http://localhost:1337/postme/'
data = {'data':'mydata'}

result = requests.post(url, json.dumps(data))