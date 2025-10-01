#zadaj cislo a spocitaj jeho cifry
number = int(input("Zadaj mi číslo: "))
scitovanie_cifier = 0
while number!= 0: #!= znamena nerovna sa
    cifra = number % 10 
    scitovanie_cifier = scitovanie_cifier + cifra
    number = number // 10 #// znamená celociselne delenie
print(scitovanie_cifier)
#doma to možem kontrolovat cez debugger
