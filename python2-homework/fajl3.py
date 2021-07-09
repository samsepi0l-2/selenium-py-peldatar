## Olvasd be a fájlt, tárold a sorokat listában, majd írd ki a lista tartalmát egy sorként egy másik fájlba!
with open("adat.txt", "r") as f:
    lista = f.readlines()

    # # sortörések nélküli megoldás
    # lista = f.read().splitlines()

with open("adat2.txt", "w") as f2:
    f2.write(str(lista))