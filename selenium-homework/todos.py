from selenium import webdriver

browser = webdriver.Chrome()


try:
    browser.get("http://localhost:9999/todo.html")

    todos = browser.find_elements_by_xpath("//li/span")

    for one_todo in todos:
        print(one_todo.text)

finally:
    browser.close()