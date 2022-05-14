from dataclasses import replace

def palindroma(fraseOr):
    frase=fraseOr.lower().replace(" ","").replace("á","a").replace("é","e").replace("í","i").replace("ó","o").replace("ú","u")
    long=len(frase)//2
    print(long)
    for n in range (long):
        if frase[n]!=frase[len(frase)-1-n]:
            Valor=False
            break
        else:
            Valor=True

    if Valor==True:    
            print(f"La frase {fraseOr} es palíndroma")
            #print(frase[n],frase[len(frase)-1-n])
    else:
        print(f"La frase {fraseOr} no es palíndroma")
    
palindroma("Sé verlos al revés")
            
#DábalE arroz a la zorra el abad
#Anita lava la tina
#Somos o no somos
#Isaac no ronca así
#Sé verlas al revés
#Amó la paloma
#Luz azul
#Yo hago yoga hoy
#Ana lava lana