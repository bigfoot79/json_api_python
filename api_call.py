import json
import requests
from sys import argv

script, end_point = argv

def get_api(url):
    response = requests.get("https://jsonplaceholder.typicode.com/todos")
    return json.loads(response.text)

print(get_api(end_point))
