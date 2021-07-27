import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()

browser.get("http://localhost:9999/simplevalidation.html")

click_out = browser.find_element_by_xpath("//h3")

email = browser.find_element_by_id("test-email")
email.send_keys("")
click_out.click()
WebDriverWait(browser, 20).until(EC.visibility_of_element_located(
    (By.XPATH, "//div[@class='validate-field-error-message' and contains(text(),'Please enter an e-mail')]")))
empty_msg = browser.find_element_by_xpath(
    "//div[@class='validate-field-error-message' and contains(text(),'Please enter an e-mail')]").text

assert empty_msg == "Please enter an e-mail"

email.send_keys("rossz")
time.sleep(1)
click_out.click()

WebDriverWait(browser, 20).until(EC.visibility_of_element_located(
    (By.XPATH, "//div[@class='validate-field-error-message' and contains(text(),'Please check your E-Mail format')]")))
validator_msg = browser.find_element_by_xpath(
    "//div[@class='validate-field-error-message' and contains(text(),'Please check your E-Mail format')]").text

assert validator_msg == "Please check your E-Mail format"

time.sleep(2)

browser.quit()
