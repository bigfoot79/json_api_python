# from the sys module, imports the argv function
from sys import argv
# import the api_call.py module and the get_api function
from api_call import get_api

# sets the argv variables for when the script is loaded.  The script variable is set automatically
# the end_point variable is the url endpoint for the json data
script, end_point = argv

# passess the end_point argv variable to the get_api function
dict = get_api(end_point)[0]

print(type(dict))
print(type(dict.values()))
