## Olvasd be a fájlt, és írd ki a tartalmát egy másik fájlba,
## úgy, hogy nem tárolod el a szöveget, hanem minden sort azonnal kiírsz!

with open("adat.txt", "r") as f1, open("adat4.txt", "w") as f2:
    f2.write(f1.read())
