from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("http://grwf.goldwindaustralia.com/Default.aspx")
assert "Central Monitor System" in driver.title

username_elem = driver.find_element_by_id("TBusername")
username_elem.send_keys('Xiaoming Zhao')

password_elem = driver.find_element_by_id("TBpassworld")
password_elem.send_keys("123456")

verify_code_img_elem = driver.find_element_by_id("yzm")
verify_code_img_url = verify_code_img_elem.get_attribute("src")

print(verify_code_img_url)


assert "No results found." not in driver.page_source
# driver.close()