import random
vidas=5

palabras=["pyton","programador","excel","random"]

palabra=random.choice(palabras)
print(palabra)

lista=list(palabra)
print(lista)

#lista=[]
#for letra in palabra:
 #   lista.append(letra)
#print(lista)

for i in range(len(lista)):
    print("_", end=" ") # end trae el salto del linea y lo reemplaza por lo que está dentro de las comillas

#print("_ "*len(lista))