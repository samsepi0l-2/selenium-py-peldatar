from selenium import webdriver
from datetime import date, datetime, time, timezone

# itt inkább firefoxot választottam, mert chrome-ban szinte az összes formátum más, mint a feladat kéri
browser = webdriver.Firefox()
browser.get("http://localhost:9999/forms.html")

mezo_date = browser.find_element_by_id("example-input-date")
mezo_date_time = browser.find_element_by_id("example-input-date-time")
mezo_local = browser.find_element_by_id("example-input-date-time-local")
mezo_month = browser.find_element_by_id("example-input-month")
mezo_week = browser.find_element_by_id("example-input-week")
mezo_time = browser.find_element_by_id("example-input-time")

# ha aktuális dátum kéne
# valami = datetime.now(timezone.utc)
# valami2 = valami.date()

datum = datetime(2021, 5, 6)
ujdatum = datetime(2012, 5, 5, 5, 5, 5, 555)
ujdatum2 = datetime(2000, 12, 5, 12, 1)
ujdatum3 = datetime(1995, 12, 2)
ujdatum4 = datetime(2015, 12, 30)
ujdatum5 = time(12,25)

# a feladatban hibásan van megadva, nem veszi be
mezo_date.send_keys(datum.strftime('%m/%d/%Y'))
mezo_date_time.send_keys(ujdatum.strftime('%Y.%m.%d. %H:%M:%S:555'))
mezo_local.send_keys(ujdatum2.strftime('%d/%m/%Y %H:%M %p'))
mezo_month.send_keys(ujdatum3.strftime('%B %Y'))
mezo_week.send_keys(ujdatum4.strftime('Week %U, %Y'))

# ezt kérné a feladat, de ez így hibás formátum
# mezo_time.send_keys(ujdatum5.strftime('%H:%M AM'))

# ezt fogadja el
mezo_time.send_keys(ujdatum5.strftime('%H:%M'))

browser.quit()