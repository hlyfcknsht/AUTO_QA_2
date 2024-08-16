import time
from selenium import webdriver
from selenium.webdriver.common.by import By

url = 'https://parsinger.ru/selenium/2/2.html'


try:
    browser = webdriver.Chrome()
    browser.get(url)
    link_text = browser.find_element(By.LINK_TEXT, "16243162441624").click()
    result = browser.find_element(By.ID, "result").text
    print(result)
    time.sleep(30)
finally:
    browser.quit()