cislo = input("Zadaj číslo: ")
sucet = 0
for cifra in cislo:
    if cifra.isdigit() and int(cifra) % 2 == 0:
        sucet += int(cifra)
print(f"Súčet párnych cifier je: {sucet}")
