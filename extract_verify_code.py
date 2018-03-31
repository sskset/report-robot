from selenium import webdriver
import requests
from PIL import Image, ImageEnhance, ImageFilter
import pytesseract
import os
import cv2

verify_code_url = "http://grwf.goldwindaustralia.com/System/VerifyCode.aspx?FM=1522498872077"
response = requests.get(verify_code_url)

verify_code_file_name = 'verify_code.jpg'
with open(verify_code_file_name, 'wb') as verify_code_file:
    verify_code_file.write(response.content)
del response

image_path = os.path.abspath(verify_code_file_name)

image = cv2.imread(image_path, 0)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

temp_vc_file_name = "{}.png".format(os.getpid())
cv2.imwrite(temp_vc_file_name, gray)

print(temp_vc_file_name)

text = pytesseract.image_to_string(Image.open(temp_vc_file_name))
print(text)
