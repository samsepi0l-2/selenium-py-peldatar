import time

from selenium import webdriver

browser = webdriver.Chrome()

browser.get("http://localhost:9999/minesweeper-game.html")


# elemek kigyűtése, és játéktér beállítása a menüben
menu = browser.find_element_by_id("menu-link")
menu.click()
custom = browser.find_element_by_id("menu-custom")
custom.click()
height = browser.find_element_by_id("minesweeper-custom-height")
height.clear()
height.send_keys("50")
width = browser.find_element_by_id("minesweeper-custom-width")
width.clear()
width.send_keys("50")
count_of_mines = browser.find_element_by_id("minesweeper-custom-mines")
count_of_mines.clear()
count_of_mines.send_keys("1")
ok_btn = browser.find_element_by_id("minesweeper-ok-btn")
ok_btn.click()


fields = browser.find_elements_by_xpath('//div[@id="minefield"]/div')  # mezők kigyűjtése listába
fields[125].click()  # 125-ös mező kattintása

# megnézzük nyertünk-e
reset = browser.find_element_by_id("minesweeper-reset-button")
smile = reset.get_attribute("class")

status = []
counter = 0

# ha nem nyertünk első kattintásra
if smile != "face-sunglasses":

    # megnézem az első kattintás után a mezők állapotát, és listába rakom
    for i in range(len(fields)):
        status.append(fields[i].get_attribute('class'))
        # még felfedetlen mező
        if status[i] == "covered":
            # ha maradt akna, akkor a valamelyik fal melletti mező a tiszta, arra kell kattintani
            if 0 <= i <= 49 or i % 50 == 0 or i % 49 == 0 or 2450 <= i <= 2499:
                fields[i].click()
                time.sleep(2)
                break

time.sleep(1)
browser.quit()