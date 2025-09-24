#obvod,obsah, vyska,typ, polomer vpisanej/ opísanej kružnice, taznice, stredne priecky 
#vlastnosti: pravouhly, rovnoramenny, rovnostranny, ostrouhly, tupouhly
import math
a = float(input("Zadaj stranu a:"))
b = float(input("Zadaj stranu b:"))
c = float(input("Zadaj stranu c:"))
#testujem či je to trojuholník
if a + b > c and a + c > b and b + c > a:
    print("Je to trojuholník")
    #testujem ci je to pravouhly
    if (a**2 + b**2 == c**2) or (a**2 + c**2 == b**2) or (b**2 + c**2 == a**2):
        print("Je to pravouhlý trojuholník")
        #testujem ci je rovnostranny
        if (a==b==c):
            print("Je to rovnostranný trojuholník")
        if (a==b and a!=c) or (a==c and a!=b) or (b==c and b!=a):
            print("Je to rovnoramenný trojuholník")
            o = a + b + c
            #po je polovicou obvodu
            po=o/2
            S=(po*(po-a)*(po-b)*(po-c))**0.5
            va=(2*S)/a
            vb=(2*S)/b
            vc=(2*S)/c
            p_vpis=S/po
            p_opis=(a*b*c)/(4*S)
            #vypocet uhlov
           uhol_a = round(math.degrees(math.acos((b**2 + c**2 - a**2)/(2*b*c))),2)
           uhol_b = round(math.degrees(math.acos((a**2 + c**2 - b**2)/(2*a*c))),2)
           uhol_c = round(math.degrees(math.acos((a**2 + b**2 - c**2)/(2*a*b))),2)
print ("Obvod je:", o)
print ("Obsah je:", S)
print ("Výška a:", va)
print ("Výška b:", vb)
print ("Výška c:", vc)
print ("Polomer vpisanej kružnice:", p_vpis)
print ("Polomer opísanej kružnice:", p_opis)
print ("Uhol a:", uhol_a)
print ("Uhol b:", uhol_b)
print ("Uhol c:", uhol_c)