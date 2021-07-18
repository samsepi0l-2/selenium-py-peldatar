from selenium import webdriver
import  time
from datetime import date, datetime, time, timezone
browser = webdriver.Chrome()
browser.get("http://localhost:9999/forms.html")

mezo_date = browser.find_element_by_id("example-input-date")
mezo_date_time = browser.find_element_by_id("example-input-date-time")
mezo_local = browser.find_element_by_id("example-input-date-time-local")
mezo_month = browser.find_element_by_id("example-input-month")
mezo_week = browser.find_element_by_id("example-input-week")
mezo_time = browser.find_element_by_id("example-input-time")

# valami = datetime.now(timezone.utc)
# valami2 = valami.date()

datum = datetime(2021, 5, 6)
print(datum.strftime('%m/%d/%Y'))
mezo_date.send_keys(datum.strftime('%m/%d/%Y'))
ujdatum = datetime(2012, 5, 5, 5, 5, 5, 555)
print(ujdatum.strftime('%Y.%m.%d. %H:%M:%S:555'))
mezo_date_time.send_keys(ujdatum.strftime('%Y.%m.%d. %H:%M:%S:555'))
ujdatum2 = datetime(2000, 12, 5, 12, 1)
print(ujdatum2.strftime('%d/%m/%Y %H:%M %p'))
ujdatum3 = datetime(1995, 12, 2)
print(ujdatum3.strftime('%B %Y'))
ujdatum4 = datetime(2015, 12, 30)
print(ujdatum4.strftime('Week %U, %Y'))
ujdatum5 = time(12,25)
print(ujdatum5.strftime('%H:%M AM'))

browser.quit()