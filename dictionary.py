vstup = input("Zadej mi retazec: ")
pocetnost = dict()

for znak in vstup:
    if ord(znak)>= 97 and ord(znak)<= 122:    # kontrola ci je to male pismeno  
       if znak in pocetnost.keys ():
           pocetnost[znak] += 1
       else:
           pocetnost[znak] = 1
print(pocetnost)


          
