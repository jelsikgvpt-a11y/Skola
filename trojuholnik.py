#obvod,obsah, vyska,typ, polomer vpisanej/ opísanej kružnice, taznice, stredne priecky 
#vlastnosti: pravouhly, rovnoramenny, rovnostranny, ostrouhly, tupouhly
import math
a = float(input("Zadaj stranu a:"))
b = float(input("Zadaj stranu b:"))
c = float(input("Zadaj stranu c:"))
#testujem či je to trojuholník
if a + b > c and a + c > b and b + c > a:
    print("Je to trojuholník")
    # Výpočet obvodu a obsahu (Heronov vzorec)
    o = a + b + c
    po = o / 2
    S = math.sqrt(po * (po - a) * (po - b) * (po - c))
    print("Obvod trojuholníka je:", o)
    print("Obsah trojuholníka je:", round(S, 2))
    # Výpočet výšok
    va = (2 * S) / a
    vb = (2 * S) / b
    vc = (2 * S) / c
    # Polomer vpísanej a opísanej kružnice
    p_vpis = S / po
    p_opis = (a * b * c) / (4 * S)
    # Výpočet uhlov
    uhol_a = round(math.degrees(math.acos((b**2 + c**2 - a**2)/(2*b*c))),2)
    uhol_b = round(math.degrees(math.acos((a**2 + c**2 - b**2)/(2*a*c))),2)
    uhol_c = round(math.degrees(math.acos((a**2 + b**2 - c**2)/(2*a*b))),2)
    print(f"Uhol pri strane a: {uhol_a}°")
    print(f"Uhol pri strane b: {uhol_b}°")
    print(f"Uhol pri strane c: {uhol_c}°")
    # Typy trojuholníka
    if (a**2 + b**2 == c**2) or (a**2 + c**2 == b**2) or (b**2 + c**2 == a**2):
        print("Je to pravouhlý trojuholník")
    if a == b == c:
        print("Je to rovnostranný trojuholník")
    elif a == b or a == c or b == c:
        print("Je to rovnoramenný trojuholník")