#vygeneruj retazec ktory bude mat od 8 do 16 znakov tak aby sa v nom striedala spoluhlaska a samohlaska
import random
spoluhlasky = "bcdfghjklmnpqrstvwxyz"
samohlasky = "aeiouy"
dlzka = random.randrange(8,17)
retazec = ""
for i in range(dlzka):
    if i%2==0:
        retazec += random.choice(spoluhlasky)
    else:
        retazec += random.choice(samohlasky)
print(retazec)
