import csv
import time
from selenium import webdriver

browser = webdriver.Chrome()
browser.get("http://localhost:9999/another_form.html")


def find_and_clear(id):
    element = browser.find_element_by_id(id)
    element.clear()
    return element


eredeti_lista = []
letoltott_lista = []
add_btn = browser.find_element_by_id("submit")
download = browser.find_element_by_xpath('//button[text()="Export HTML table to CSV file"]')

with open("table_in2.csv", "r", encoding="utf-8") as tablazat:
    adatok = csv.reader(tablazat, delimiter=",")
    next(adatok)
    for row in adatok:
        eredeti_lista.append(row)
        find_and_clear("fullname").send_keys(row[0])
        find_and_clear("email").send_keys(row[1])
        find_and_clear("dob").send_keys(row[2])
        find_and_clear("phone").send_keys(row[3])
        add_btn.click()

# # Letöltés tesztelése
# download.click()
# time.sleep(1)
#
# counter = 1
# try:
#     with open("C:\\Users\\user\\Downloads\\table.csv", "r", encoding="utf-8") as letoltes:
#         with open("table_in2.csv", "r", encoding="utf-8") as tablazat:
#             adatok = csv.reader(tablazat, delimiter=",")
#             letoltott_adatok = csv.reader(letoltes, delimiter=",")
#
#             # a két táblázat összehasonlítása soronként
#             for i in letoltott_adatok:
#                 print(f"Letöltött csv file {counter}. sora: ")
#                 print(i)
#                 for k in adatok:
#                     print(f"Eredeti csv file {counter}. sora: ")
#                     print(k)
#                     try:
#                         assert i == k
#                     except:
#                         print(f"HIBA: Egyezési hiba a a táblázatok közt a {counter}. sorban")
#                     counter += 1
#                     print("\n")
#                     break
# except:
#     print("Valami nem működik")

browser.quit()
