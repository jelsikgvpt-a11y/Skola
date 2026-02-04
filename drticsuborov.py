fr = open("subory/data.txt", "r", encoding="utf-8")
# Čítanie obsahu súboru od začiatku
#prvý spôsob
#for row in fr:
    #print (row)

#druhý spôsob
#jozo = fr.readlines()
#vytvorim list, ktoreho prvkami su cele riadky suboru
#print(jozo)

#tretí spôsob
#first_line = fr.readline()
#print(first_line)
#for row in fr: #ide od druheho riadku
    #print(row)

def is_cool (word):
    for i in range (len(word)-1): #-1 lebo porovnavam s dalsim pismenom a posledne už nema s cim porovnat
        if word[i] > word[i+1]:
            return False
    return True





words = 0
words_no_e = 0
words_e = 0
for row in fr:
    row = row.strip()  # odstránil som posledny enter
    words += 1
    if 'e' in row:
        words_e += 1
    else:
        words_no_e += 1

print(words_no_e)
print(words_e)
print(is_cool("abbde"))