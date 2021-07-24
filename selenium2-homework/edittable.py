import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()

browser.get("http://localhost:9999/editable-table.html")
add_btn = browser.find_element_by_xpath("//button[@class='btn btn-success pull-right']")
alap = browser.find_elements_by_xpath("//table/tbody/tr")
add_btn.click()
add_btn.click()

table = browser.find_elements_by_xpath("//table/tbody/tr")

# Sor hozzáadás ellenőrzése
try:
    assert len(table) == len(alap) + 2
    print("Test1: A sorok létrejöttek")
except AssertionError:
    print("HIBA: A sorok nem jöttek létre")

# Új sorok feltöltése
for i in table:
    cellak = i.find_elements_by_tag_name("input")
    cellak[0].get_attribute("value")
    if cellak[0].get_attribute("value") == "":
        cellak[0].send_keys("gyros")
        cellak[1].send_keys("1.99")
        cellak[2].send_keys("110")
        cellak[3].send_keys("Food")

search = browser.find_element_by_xpath("//input[@placeholder='Search...']")
search.send_keys("gyros")
# time.sleep(2)

filtered = browser.find_elements_by_xpath("//table/tbody/tr")

# keresőmező ellenőrzése
try:
    assert len(filtered) == 2
    print("Test2: A név szerinti szűrés működik")
except AssertionError:
    print("HIBA: A név szerinti szűrés nem működik")

# clear() függvénnyel nem leet szimulálni a szűrő mező
for i in "gyros":
    search.send_keys(Keys.BACK_SPACE)
# time.sleep(2)

all_record_list = browser.find_elements_by_xpath("//table/tbody/tr/td/input")
szoveg = all_record_list[0].get_attribute("value")
all_record_list[0].send_keys("valami")

# DOM struktúra változásának ellenőrzése szövegbevitelnél
try:
    assert all_record_list[0].get_attribute("value") == f"{szoveg}valami"
    print("Test3: Szöveg bevitele után a DOM struktúra megfelelően frissült")
except AssertionError:
    print("HIBA: Szöveg bevitele után a DOM struktúra nem frissült")

# time.sleep(2)
browser.quit()