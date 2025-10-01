#zisti ci cislo je prvocislo
number = int(input("Zadaj mi číslo: "))
count_numbers = 0
for delitel in range(2, number):
    if number % delitel == 0:
        count_numbers += 1
if count_numbers == 0:
    print("Je to prvočíslo")
else:
    print("Nie je to prvočíslo")