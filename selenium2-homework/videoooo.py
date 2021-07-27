import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()

browser.get("http://localhost:9999/videos.html")
browser.maximize_window()

video_1 = browser.find_element_by_id("html5video")
video_1.click()
time.sleep(4)
video_1.send_keys(Keys.SPACE)
time.sleep(1)

video_2_play_pause = browser.find_element_by_xpath("//button[contains(text(), 'Play')]")
video_2_play_pause.click()
time.sleep(4)
video_2_play_pause.click()
time.sleep(1)

video_3 = browser.find_element_by_id("youtubeframe")
video_3.click()
time.sleep(6)
video_3.click()
time.sleep(3)

browser.quit()