from selenium import webdriver

browser = webdriver.Chrome()

browser.get("http://localhost:9999/")

links = browser.find_elements_by_xpath("//a")

with open("linkek.txt", "w") as lin:
    for i in links:
        lin.write(i.get_attribute("href"))
        lin.write("\n")

print(f"Az oldal {len(links)} darab linket tartalmaz")
browser.quit()