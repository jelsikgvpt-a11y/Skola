
def stvorec(n:int, znak:str) -> str:
    vysledok = ""
    for i in range(0,n):
        if i == 0 or i == n-1:
            vysledok += znak*n
            vysledok += "\n"
    else:
        vysledok += znak +(n-2)*" " + znak + "\n"
    return vysledok
print(stvorec(5,"#"))




    