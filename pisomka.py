#napíš funkciu kde retazec bude vstupny parameter a funkcia vrati retazec kde male písmená budú vymenene za velke a male zas opacne
#ostatne znaky ostanu nezmenene
def zamen_male_velke(retazec):
    novy_retazec = ""
    for znak in retazec:
        if znak.islower():
            novy_retazec += znak.upper()
        elif znak.isupper():
            novy_retazec += znak.lower()
        else:
            novy_retazec += znak
    return novy_retazec

#test
vstup = "mILujem Fica! 123"
vystup = zamen_male_velke(vstup)
print(vystup) 
    