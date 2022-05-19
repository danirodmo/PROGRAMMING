import random
numBingo=[x for x in range(1,76)]
balotas=[]
print(numBingo)

Sel=input("¿Desea sortear una balota? Digite S o N : ").upper()



if Sel=="S":
        balota=random.choice(numBingo)
        print(balota)
        balotas.append(balota)
        print(balotas)
        numBingo.remove(balota)
        print(numBingo)
else:
    print("Fin del Juego")