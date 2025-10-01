# Spočíta prvočísla v zadanom intervale
zaciatok = int(input("Zadaj mi začiatok intervalu: "))
koniec = int(input("Zadaj mi koniec intervalu: "))
sucet = 0

def je_prvocislo(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

for cislo in range(zaciatok, koniec + 1):
    if je_prvocislo(cislo):
        sucet += cislo
print(f"Súčet prvočísel v intervale je: {sucet}")
