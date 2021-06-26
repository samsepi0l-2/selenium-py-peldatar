from selenium import webdriver

browser = webdriver.Chrome()

browser.get("http://localhost:9999/trickyelements.html")

elem1 = browser.find_element_by_id("element1")
elem2 = browser.find_element_by_id("element2")
elem3 = browser.find_element_by_id("element3")
elem4 = browser.find_element_by_id("element4")
elem5 = browser.find_element_by_id("element5")
result1 = browser.find_element_by_id("result")

if elem1.tag_name == "button":
    elem1.click()
    if result1.text == f"{elem1.text} was clicked":
        print(result1.text)
        print("Szöveg OK")
    else:
        print("Hibás szöveg")
    browser.quit()
elif elem2.tag_name == "button":
    elem2.click()
    if result1.text == f"{elem2.text} was clicked":
        print(result1.text)
        print("Szöveg OK")
    else:
        print("Hibás szöveg")
    browser.quit()
elif elem3.tag_name == "button":
    elem3.click()
    if result1.text == f"{elem3.text} was clicked":
        print(result1.text)
        print("Szöveg OK")
    else:
        print("Hibás szöveg")
    browser.quit()
elif elem4.tag_name == "button":
    elem4.click()
    if result1.text == f"{elem4.text} was clicked":
        print(result1.text)
        print("Szöveg OK")
    else:
        print("Hibás szöveg")
    browser.quit()
elif elem5.tag_name == "button":
    elem5.click()
    if result1.text == f"{elem5.text} was clicked":
        print(result1.text)
        print("Szöveg OK")
    else:
        print("Hibás szöveg")
    browser.quit()
else:
    print("Nincs gomb")

browser.quit()