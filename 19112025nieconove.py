#2 typy šifrovania: symetricke a asymetricke
#Symetricke - na šifrovanie a dešifrovanie sa používa rovnaký kľúč
#Asymetricke - na šifrovanie a dešifrovanie sa používajú rôzne kľúče 2: verejný a privátny
#co je hashovanie - hashovanie je proces prevodu dát na pevne dlhý reťazec znakov, ktorý reprezentuje pôvodné dáta
#na čo sa používa hashovanie - na zabezpečenie integrity dát, ukladanie hesiel, digitálne podpisy a ďalšie bezpečnostné aplikácie
#zvysok po celociselnom deleni nas zaujima
def vyhod_duplikaty(retazec:str) -> str:
    vysledok = retazec[0]
    for i in range (1, len(retazec)):
        if retazec[i] != vysledok[-1]:
            vysledok += retazec[i]
    return vysledok
print(vyhod_duplikaty("aaabbbccddeeefff"))

