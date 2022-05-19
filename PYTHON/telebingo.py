import random
numBalotas=[x for x in range(1,76)]
balotasJugadas=[]
print(numBalotas)
for balota in range (1,76):
    Pregunta=input("¿Desea sortear una nueva balota? S/N ").upper()
    if Pregunta!="N":
        balota=random.choice(numBalotas)
        if balota>0 and balota<=15:
            print(f"B{balota}")
            balotasJugadas.append("B"+str(balota))
        elif balota>15 and balota<=30:
            print(f"I{balota}")
<<<<<<< HEAD
            balotasJugadas.append("I",str(balota))
=======
            balotasJugadas.append("I"+str(balota))
>>>>>>> 7ed655796b3627ea3bdb603fa88d6ec6f3a9f4cb
        elif balota>30 and balota<=45:
            print(f"N{balota}")
            balotasJugadas.append("N"+str(balota))
        elif balota>45 and balota<=60:
            print(f"G{balota}")
            balotasJugadas.append("G"+str(balota))
        else:
            print(f"O{balota}")
            balotasJugadas.append("O"+str(balota))
    
    else:
        print("Fin del Juego")
        break

    print(f"Balotas jugadas: {balotasJugadas}")
    numBalotas.remove(balota)        
    print(numBalotas)