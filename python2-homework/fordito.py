szam = 1
lista = []
szoveg = ""
try:
    while szam != 0:
        if szam > 0:
            szam = int(input("Írj be egy pozitív számot, vagy ha kilépnél, írj be 0-át: "))
            if szam != 0 and szam > 0:
                lista.append(szam)
        else:
            print("Ez a szám negatív")
            break
except:
    print("Hibás bemenet")

finally:
    #1. megoldás slice-al [start:stop:step]
    forditott = lista[::-1]
    print(f"A fordított lista: {forditott}")


    ##2. megoldás függvénnyel
    # lista.reverse()
    # print(f"A fordított lista: {lista}")

