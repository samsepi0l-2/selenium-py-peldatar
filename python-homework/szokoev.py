def szokoev(evszam):
    if evszam % 4 == 0:
        return "True"
    else:
        return "False"


bemenet = int(input("Írj be egy évszámot: "))
# kimenet = szokoev(bemenet)
print(szokoev(bemenet))