#!/usr/bin/python3


import requests
import pytesseract
try:
        from PIL import Image
except ImportError:
        import Image

URL = 'http://158.69.76.135/level5.php'
captcha_url = 'http://158.69.76.135/captcha.php'
windows_user = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                "(KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36")
header = {'User-Agent': windows_user, 'Referer': URL}
api_key = '174faff8fbc769e94a5862391ecfd010'

for i in range(5):
    try:
        # start request session
        with requests.Session() as session:
            # get the response object
            response = session.get(URL, headers=header)

            image = session.get(captcha_url, headers=header)

            image_file = open('captcha.png', 'wb')
            image_file.write(image.content)
            image_file.close()

            captcha = pytesseract.image_to_string(Image.open('captcha.png'))
            captcha = captcha.replace(" ", "").strip()

            site_key = response.cookies['HoldTheDoor']

            my_data = {
                'id': '2282', 'key': site_key,
                'captcha': captcha, 'holdthedoor': 'submit'}
            # send data
            response_post = session.post(URL, headers=header, data=my_data)
            print('Status: {}'.format(response_post.status_code))
    except Exception as error:
        print(error)
        i -= 1
print("Cheat online voting process finished :)")