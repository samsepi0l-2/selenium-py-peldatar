import time

from selenium import webdriver
import os.path
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()

browser.get("http://localhost:9999/scrolltoload.html")

# time.sleep(2)
WebDriverWait(browser, 20).until(EC.visibility_of_all_elements_located((By.CLASS_NAME, "image")))
scrolling = "window.scrollTo(0, 2000);"
time.sleep(3)
browser.execute_script(scrolling)
time.sleep(3)
all_img = browser.find_elements_by_xpath("//div[@class='image']/img")
time.sleep(2)
all_id = browser.find_elements_by_xpath("//div[@class='image']/p")
first_img = all_img[1].get_attribute("src")

# time.sleep(2)
for i in range(20):
    time.sleep(0.3)
    sorszam = i + 1
    id = all_id[i].text[8:]
    with open(f".\\cat2\\{sorszam}_{id}.png", 'wb') as file:
        file.write(all_img[i].screenshot_as_png)

# time.sleep(20)
browser.close()