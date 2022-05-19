import os
def materias (materias):
    os.system("cls")
    Lista=materias.split(",")
    return Lista

print (materias("Inglés,Física,Sociales,Historia,Programación"))
