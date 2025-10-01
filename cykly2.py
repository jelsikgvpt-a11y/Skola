zaciatok = int(input("Zadaj mi cislo: "))
koniec = int(input("Zadaj mi cislo: "))
vystup = 0
for i in range(zaciatok, koniec + 1):
    vystup = vystup + i #vystup += i
print(vystup)