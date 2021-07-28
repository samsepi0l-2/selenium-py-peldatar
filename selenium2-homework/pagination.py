from selenium import webdriver
import pprint
import time
import csv

browser = webdriver.Chrome()

extracted_data = []

try:
    browser.get("http://localhost:9999/pagination.html")
    while True:
        time.sleep(0.3)
        table = browser.find_element_by_xpath("//table[@id='contacts-table']/tbody")
        rows = table.find_elements_by_tag_name("tr")
        for row in rows:
            data_row = {}
            cells = row.find_elements_by_tag_name("td")
            if cells[1].text.startswith("A"):
                data_row["id"] = cells[0].text
                data_row["first_name"] = cells[1].text
                data_row["second_name"] = cells[2].text
                data_row["surname"] = cells[3].text
                data_row["second_surname"] = cells[4].text
                data_row["birth_date"] = cells[5].text
                extracted_data.append(data_row)
        next_button = browser.find_element_by_id("next")
        if not next_button.is_enabled():
            break
        else:
            next_button.click()

    pprint.pp(extracted_data)
    print(len(extracted_data))

    csv_columns = ['id', 'first_name', 'second_name', 'surname', 'second_surname', 'birth_date']
    with open('a_names.csv', 'w', encoding = 'utf-8') as new_csv:
        writer = csv.DictWriter(new_csv, fieldnames=csv_columns)
        writer.writeheader()
        for i in extracted_data:
            writer.writerow(i)
finally:
    browser.close()