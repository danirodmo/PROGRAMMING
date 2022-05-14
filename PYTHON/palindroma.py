from dataclasses import replace

def palindroma(fraseOr):
    frase=fraseOr.lower().replace(" ","").replace("á","a").replace("é","e").replace("í","i").replace("ó","o").replace("ú","u")
    long=len(frase)//2
    for n in range (long):
        if frase[n]!=frase[len(frase)-1-n]:
            esPalindroma=False
            break
        else:
            esPalindroma=True

    if esPalindroma==True:    
            print(f"La frase {fraseOr} es palíndroma")
    else:
        print(f"La frase {fraseOr} no es palíndroma")
    
palindroma("Yo haGo Yogá hoy")

'''FRASES PALÍNDROMAS:            
DábalE arroz a la zorra el abad
Anita lava la tina
Somos o no somos
Isaac no ronca así
Sé verlas al revés
Amó la paloma
Luz azul
Yo hago yoga hoy
Ana lava lana
'''