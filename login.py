from selenium import webdriver
from PIL import Image
from verify_code import VerifyCode
import time

is_ready_to_login = False

while not is_ready_to_login:
    browser = webdriver.Chrome()
    browser.set_window_size(572, 400)
    browser.get("http://grwf.goldwindaustralia.com/Default.aspx")
    # time.sleep(1)

    username_elem = browser.find_element_by_id('TBusername')
    username_elem.send_keys('Xiaoming Zhao')

    password_elem = browser.find_element_by_id('TBpassworld')
    password_elem.send_keys('123456')

    code_img_elem = browser.find_element_by_id('yzm')

    browser.save_screenshot('images/login_page.png')

    location = code_img_elem.location
    size = code_img_elem.size

    print("location:{} size:{}".format(location, size))

    left = location['x'] * 2 + 4
    top = location['y'] + 53
    # right = left + size['width']
    # bottom = top + size['height']
    right = left + 115
    bottom = top + 30

    # print(left, top, right, bottom)

    im = Image.open('images/login_page.png')  # uses PIL library to open image in memory
    im = im.crop((left, top, right, bottom))  # defines crop points
    im.save('images/code.gif')  # saves new cropped image

    code = VerifyCode.get_text_from_image_file('images/code.gif')

    print(code)
    # time.sleep(3)

    code_elem = browser.find_element_by_id("TBvalidate")
    code_elem.send_keys(code)

    if len(code) == 4:
        login_button_elem = browser.find_element_by_xpath(
            '//*[@id="form1"]/table/tbody/tr[2]/td[2]/table/tbody/tr[2]/td/table/tbody/tr/td[3]/table/tbody/tr/td[2]')
        print(login_button_elem.text)
        login_button_elem.click()

        is_ready_to_login = True

    else:
        browser.close()
