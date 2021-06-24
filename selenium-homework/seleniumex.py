def id_search_try(element_id):
  try:
    id_kereses = browser.find_element_by_id(element_id)
    print(id_kereses)
  except:
    print("Az id nem létezik")

from selenium import webdriver

browser = webdriver.Chrome()

browser.get("https://telex.hu")

id_search_try("nemletezik")
browser.close()