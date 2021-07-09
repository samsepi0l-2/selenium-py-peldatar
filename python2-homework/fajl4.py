## Olvasd be a fájlt, tárold a sorokat listában, majd írd ki a lista tartalmát így,
## ahogy beolvastad, soronként egy szóval egy másik fájlba!

with open("adat.txt", "r") as f:
    lista = f.readlines()

with open("adat3.txt", "w") as f2:
    for i in lista:
        f2.write(i)