import time

from selenium import webdriver
from selenium.webdriver.common import actions
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

browser = webdriver.Chrome()

browser.get("http://localhost:9999/alert_playground.html")

alert_btn = browser.find_element_by_xpath("//input[@name= 'alert']")
confirmation_btn = browser.find_element_by_xpath("//input[@name= 'confirmation']")
promt_btn = browser.find_element_by_xpath("//input[@name= 'prompt']")
double_click_btn = browser.find_element_by_xpath("//*[@id='double-click']")
paragraph = browser.find_element_by_id("demo")

alert_btn.click()
time.sleep(1)
alert_window = browser.switch_to.alert
alert_window.accept()
time.sleep(1)

confirmation_btn.click()
time.sleep(1)
confirmation_window = browser.switch_to.alert
confirmation_window.accept()
time.sleep(1)

confirmation_btn.click()
time.sleep(1)
confirmation_window = browser.switch_to.alert
confirmation_window.dismiss()
time.sleep(1)

promt_btn.click()
time.sleep(1)
promt_window = browser.switch_to.alert
promt_window.send_keys("Helloka")
promt_window.accept()
try:
    assert paragraph.text == "You entered: Helloka"
    print("A prompt bevitel működött")
except:
    print("HIBA: A bevitt szöveg nem jelent meg")

promt_btn.click()
time.sleep(1)
promt_window = browser.switch_to.alert
promt_window.send_keys("Belloka")
promt_window.dismiss()

try:
    assert paragraph.text == "You entered: Helloka"
    print("A prompt dismiss bevitel esetén is működött")
except:
    print("HIBA: A dismiss sikertelen")

action_click = ActionChains(browser)
action_click.double_click(double_click_btn).perform()
double_window = browser.switch_to.alert
time.sleep(1)
double_window.dismiss()

time.sleep(1)
browser.quit()