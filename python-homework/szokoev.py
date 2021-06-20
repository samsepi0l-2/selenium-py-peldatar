def szokoev(evszam):
    if (evszam % 4 == 0) and (evszam % 100 != 0):
        return True
    elif (evszam % 400 == 0):
        return True
    else:
        return False
eredmeny = ""
counter = int(input("Hány darab évszámra vagy kíváncsi?: "))
for i in range(counter):
    bemenet = int(input("Írj be egy évszámot: "))
    if szokoev(bemenet) == True:
        kimenet = "Szökőév"
    else:
        kimenet = "Nem szökőév"
    eredmeny = eredmeny + (f"{bemenet}: {kimenet}; ")
print(eredmeny)
