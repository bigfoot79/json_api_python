# imports the json module
import json
# imports the requests module
import requests
# from the sys module, imports the argv function
from sys import argv

# sets the argv variables for when the script is loaded.  The script variable is set automatically
# the end_point variable is the url endpoint for the json data
script, end_point = argv

def get_api(url):
    """ Returns the url endpoint data as a list of dictionaries
        which represent the json data in key value pairs

        The argument is the url for the endpoint.  This is parsed
        through argv on running the script itself.

        Uses the requests function to obtain the raw json dataself.
        Uses the json.loads function to convert the raw data into a
        list of dictionaries.
    """
    response = requests.get(url)

    return json.loads(response.text)

print(get_api(end_point))

print(len(get_api(end_point)))

print(type(get_api(end_point)))

print(get_api(end_point)[0])
