kor = int(input("Hány éves vagy?: "))
ital = input("Milyen italt kérsz?: ")

if ital != "sör" and ital != "kóla":
    print("Csak sör és kóla van")
elif kor < 18 and ital == "sör":
    print("Kiskorút nem szolgálhatunk ki alkohollal")
elif kor > 60 and ital == "kóla":
    print(f"A koffein megemelheti a vérnyomását, a {ital}-t nem ajánlom")
else:
    print(f"Parancsoljon, itt a {ital}!")
