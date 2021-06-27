from selenium import webdriver

browser = webdriver.Chrome()

browser.get("http://localhost:9999/kitchensink.html")

elem1 = browser.find_element_by_id("multiple-select-example")
print(f"A(z) {elem1.tag_name} típusú elemben található szöveg: \n{elem1.text}")
print("-"*50)

elem2 = browser.find_element_by_name("enter-name")
print(f"A {elem2.location} lokáción található {elem2.tag_name} típusú elem placeholder szövege: ")
print(elem2.get_attribute("placeholder"))
print("-"*50)

elem3 = browser.find_element_by_id("hide-textbox")
elem3.click()

#elem4 = browser.find_element_by_xpath("//input[@style='display: none;']")
elem4 = browser.find_element_by_xpath("//*[@id='displayed-text']")
rejtett_placeholder= elem4.get_attribute("placeholder")

print(f"A {elem4.size} méretű rejtett {elem4.tag_name} elem placeholder szövege: {rejtett_placeholder}")

browser.quit()