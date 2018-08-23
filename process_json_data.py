# from the sys module, imports the argv function
from sys import argv
# import the api_call.py module and the get_api function
from api_call import get_api

# sets the argv variables for when the script is loaded.  The script variable is set automatically
# the end_point variable is the url endpoint for the json data
script, end_point = argv
# "https://jsonplaceholder.typicode.com/todos" - url end point for api resource
# passess the end_point argv variable to the get_api function

# api_content is a list of dictionaries which contain the json key value pairs
api_content = get_api(end_point)

# counts the number of dictionaries included in the api_content list
number_of_elements = len(api_content)
# counter to iterate through the list of dictionaries
i = 0

# counter to count the number of False tasks
not_completed = 0

# for loop to iterate through the list of dictionaries and count the number
# of dictionaries with key: 'completed' = False
for element in api_content:
    dict_loop = api_content[i]
    if dict_loop['completed'] == False:
        not_completed += 1
    i += 1

# calculates the number of completed tasks by subtracting the not_completed tasks
# from the number_of_elements.  This provides the number of completed tasks
completed_tasks = number_of_elements - not_completed

# prints a variety of variables
print("There are " + str(number_of_elements) + " todos.")
print("There are " + str(not_completed) + " tasks which have not been completed")
print("There are " + str(completed_tasks) + " which have been completed")
