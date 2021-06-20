szam = 0
osszeg = 0

# Ha az a feladat, hogy a ciklus addig fusson, amíg az adott beolvasás kisebb mint 10
while szam < 10:
    szam = int(input("Írj be egy számot: "))
    osszeg = osszeg + szam

print(osszeg)

# Ha az a feladat, hogy a ciklus addig fusson, amíg a beolvasások összege kisebb mint 10
# while osszeg < 10:
#     szam = int(input("Írj be egy számot: "))
#     osszeg = osszeg + szam
#
# print(osszeg)