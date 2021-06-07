#!/usr/bin/python3
'''
Program to vote 4096 times
to the Hodor project from
Holberton School
'''
# Import module
import requests

# Level 1
times = 1
URL = 'http://158.69.76.135/level1.php'

for i in range(times):
    try:
        with requests.Session() as session:
            # Get the response object by get method
            r = session.get(URL)
            # Obtaining the key from cookies
            key = session.cookies['HoldTheDoor']
            # Composing the data that will be send
            my_id = {'id': 2282, 'key': key, 'holdthedoor': 'submit'}
            # Send the data
            response_post = session.post(URL, data=my_id)

    except Exception as error:
        print(error)
    print(response_post.headers)
    print("Status: {} of 4096".format(i + 1))
    print('Post request status: {}'.format(response_post.status_code))
print("Cheat online voting process finished :)")
