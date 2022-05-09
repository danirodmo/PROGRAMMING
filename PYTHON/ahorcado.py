import random
vidas=5

palabras=["python","programador","excel","random","anaconda","reto"]

palabra=random.choice(palabras)
print(palabra)

#listaPalabra=list(palabra)
#listaGuion=[]
#print(listaPalabra)
listaGuion=[]
listaPalabra=[]
for letraIngresada in palabra:
   listaPalabra.append(letraIngresada)
   listaGuion.append("_")
print(listaPalabra)
print(listaGuion)
contador=1
while contador<=vidas:
    letraIngresada=input("Ingrese una letra: ")
    for letra in range(len(listaPalabra)): 
        if listaPalabra[letra]==letraIngresada:
            listaGuion[letra]=letraIngresada
    print(listaGuion)
            


'''    for i in range(len(listaPalabra)):
        print("_", end=" ") # end trae el salto del linea y lo reemplaza por lo que está dentro de las comillas
#print("_ "*len(listaPalabra))
''' 