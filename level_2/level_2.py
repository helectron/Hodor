#!/usr/bin/python3
''' 
Program to vote 1024 times
to the Hodor project from
Holberton School
'''
# Import module
import requests

# Level 2
times = 1024
URL = 'http://158.69.76.135/level2.php'
windows_user = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                "(KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36")
header = {"User-Agent": windows_user, "Referer": URL}
for i in range(times):
    try:
        with requests.Session() as session:
            # Get the response object by get method
            r = session.get(URL, headers=header)
            # Obtaining the key from cookies
            key = session.cookies['HoldTheDoor']
            # Composing the data that will be send
            my_id = {'id': 2282, 'key': key, 'holdthedoor': 'submit'}
            # Send the data
            response_post = session.post(URL, data=my_id, headers=header)

    except Exception as error:
        print(error)
    print(response_post.headers)
    print("Status: {} of 1024".format(i + 1))
    print('Post request status: {}'.format(response_post.status_code))
print("Cheat online voting process finished :)")
