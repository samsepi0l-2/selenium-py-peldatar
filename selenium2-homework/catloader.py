import time

from selenium import webdriver
import os.path
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()

browser.get("http://localhost:9999/loadmore.html")

# time.sleep(2)
WebDriverWait(browser, 20).until(EC.visibility_of_all_elements_located((By.CLASS_NAME, "image")))
more_btn = browser.find_element_by_xpath("//div[@class= 'load-more-button']/button")
more_btn.click()
WebDriverWait(browser, 20).until(EC.visibility_of_all_elements_located((By.CLASS_NAME, "image")))
more_btn.click()
WebDriverWait(browser, 20).until(EC.visibility_of_all_elements_located((By.CLASS_NAME, "image")))
more_btn.click()
WebDriverWait(browser, 20).until(EC.visibility_of_all_elements_located((By.CLASS_NAME, "image")))
all_img = browser.find_elements_by_xpath("//div[@class='image']/img")
time.sleep(2)
all_id = browser.find_elements_by_xpath("//div[@class='image']/p")
first_img = all_img[1].get_attribute("src")

# time.sleep(2)
for i in range(len(all_img)):
    time.sleep(0.3)
    sorszam = i + 1
    id = all_id[i].text[8:]
    with open(f".\\cat\\{sorszam}_{id}.png", 'wb') as file:
        file.write(all_img[i].screenshot_as_png)

# time.sleep(20)
browser.close()
