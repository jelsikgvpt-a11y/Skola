import random 
zoz = []
for i in range (10):
    zoz.append(random.randrange(1, 101))
print(zoz)

zoz_par = 0 
zoz_indx_par = 0
for i in range (len(zoz)):
    if zoz[i]%2 == 0:
        zoz_par += zoz [i]
    if i % 2 ==0:
        zoz_indx_par += zoz [i]
print()

