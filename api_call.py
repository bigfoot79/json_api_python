# imports the json module
import json
# imports the requests module
import requests

def get_api(url):
    """ Returns the url endpoint data as a list of dictionaries
        which represent the json data in key value pairs.

        The argument is the url for the endpoint.  This is parsed
        through argv on running the script itself.

        Uses the requests function to obtain the raw json dataself.
        Uses the json.loads function to convert the raw data into a
        list of dictionaries.
    """
    response = requests.get(url)

    return json.loads(response.text)
