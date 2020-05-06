import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/explicit_wait2.html")
message = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), '100'))
button = WebDriverWait(browser, 12).until(EC.element_to_be_clickable((By.ID, 'book')))
button.click()
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))
x_element = browser.find_element_by_css_selector('.container .form-group #input_value')
x = x_element.text
y = calc(x)
input1 = browser.find_element_by_css_selector('#answer')
input1.send_keys(y)
button1 = browser.find_element_by_css_selector("#solve")
button1.click()