# 23
from itertools import cycle
def posuvac(znak, posun):
    if "a" <= znak <= "z" and znak.islower():
        stary_index = ord(znak) - ord("a")
        novy_index = (stary_index + posun) % 26
        nove_pismenko = chr(novy_index + ord("a"))
        return nove_pismenko
    else:
        return znak

def sifrovac(nacitane_riadky):
    kluc = input("Zadajte šifrovací kľúč (iba malé písmenká): ")
    vysledok =[]
    kluc_zacykleny = cycle(kluc)
    for riadok in nacitane_riadky:
        temp_riadok = []

        for znak in riadok:
            posun = ord(next(kluc_zacykleny)) - ord("a") + 1
            novy_znak = posuvac(znak, posun)
            temp_riadok.append(novy_znak)
        
        vysledok.append(("").join(temp_riadok))
    return vysledok

def desifrovac(nacitane_riadky):
    kluc = input("Zadajte šifrovací kľúč (iba malé písmenká): ")
    kluc_zacykleny = cycle(kluc)
    vysledok =[]
    for riadok in nacitane_riadky:
        temp_riadok = []

        for znak in riadok:
            posun = -(ord(next(kluc_zacykleny)) - ord("a") + 1)
            novy_znak = posuvac(znak, posun)
            temp_riadok.append(novy_znak)
        
        vysledok.append(("").join(temp_riadok))
    return vysledok

vstup_sifrovat = "vstupny_text.txt"
vstup_desifrovanie = "zasifrovany_text_1.txt"
vystup = "vystup.txt"

def otvarac(vstup):
    with open (vstup, "r", encoding = "UTF-8") as fr:
        nacitane_riadky = fr.readlines()
    print("Prečítané.")
    return nacitane_riadky

def pisac(vystup, riadky):
    with open(vystup, "w", encoding = "UTF-8") as fw:
        for riadok in riadky:
            fw.write(riadok)
        print("Zapísané.")

co = input("Napíš 1 ak chceš šifrovať, ak dešifrovať, napíš 2: ")
if co == "1":
    nacitane_riadky = otvarac(vstup_sifrovat)
    vysledok = sifrovac(nacitane_riadky)
    pisac(vystup, vysledok)
elif co == "2":
    nacitane_riadky = otvarac(vstup_desifrovanie)
    vysledok = desifrovac(nacitane_riadky)
    pisac(vystup, vysledok)
else:
    print("Zadaj buď 1 alebo 2!")