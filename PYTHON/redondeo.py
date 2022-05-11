from random import random
listaNotas=[]
listaEstudiantes=[]
nEstudiantes=70

for i in range (nEstudiantes):
    listaNotas.append(round(random.uniform(0.0,5.0),1))
print(listaNotas)