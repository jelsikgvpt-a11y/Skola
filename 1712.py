#nejaký bubble sort začíname
import random
def generuj(n:int) -> list:
    zoz = []
    for i in range(n):
        zoz.append(random.randint(1, 100))
    return zoz

moj_zoz = generuj(10)
print(moj_zoz)

    
def uprac(zoz:list, dlzka:int):
    for i in range(0, dlzka-1):
        if zoz[i] > zoz[i+1]:
            zoz[i], zoz[i+1] = zoz[i+1], zoz[i]
for j in range(len(moj_zoz),1,-1):
    uprac(moj_zoz, j)
print(moj_zoz)