def rozsekaj (text:str, sirka:int) -> str:
    vysledok = ""
    for i in range(0, len(text), sirka):
        vysledok += text[i:i+sirka]  
        vysledok += "\n"
    return vysledok

print(rozsekaj("Anicka dusicka kde si bola", 10))     

        
  