def vyhod_duplikaty(retazec:str) -> str:
    vysledok = retazec[0]
    for i in range (1, len(retazec)):
        if retazec[i] != vysledok[-1]:
            vysledok += retazec[i]
    return vysledok
print(vyhod_duplikaty("aaabbbccddeeefff"))
           
       