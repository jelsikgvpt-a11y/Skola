vstup = int(input("Zadaj mi číslo: "))
vystup = 1
for i in range(1, vstup + 1):
    vystup = vystup * i #vystup *= i
print(vystup)
