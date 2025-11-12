def faktorial(n):
    vysledok = 1
    for i in range(2, n + 1):
        vysledok *= i
    return vysledok

def kombCislo (n, k):
    return faktorial(n) // (faktorial(k) * faktorial(n - k))

cislo = kombCislo(10, 2)
print(cislo)


pokus= faktorial(10)
print(pokus)
#pascalov trojuholnik

def PasTroj(velkost):
    for riadok in range (velkost):
        for cislo in range (0, riadok+1):
           print(kombCislo(riadok, cislo), end=" ")
        print()

PasTroj(5)
