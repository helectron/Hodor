#!/usr/bin/python3

# Import module
import requests

# Level 0
times = 5
my_id = {
    'id': '2282',
    'holdthedor': 'submit'
}
url = 'http://158.69.76.135/level0.php'

for i in range(times):
    get_response = requests.post(url, data = my_id)
