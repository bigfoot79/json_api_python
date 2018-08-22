import json
import requests
from sys import argv

script, end_point = argv

def get_api(url):
    response = requests.get(url)
    return json.loads(response.text)

print(get_api(end_point))
print(type(get_api(end_point)))
