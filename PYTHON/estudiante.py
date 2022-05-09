numeroEstudiantes=int(input("Cuantos estudiantes hay? "))
contA=0
contP=0
notaE=0
for estudiante in range (numeroEstudiantes):
    nota1=float(input("Digita tu nota 1: "))
    nota2=float(input("Digita tu nota 2: "))
    nota3=float(input("Digita tu nota 3: "))
    promedioNotas=(nota1*.20)+(nota2*.30)+(nota3*.50)
    print(f"Definitva estudiante {estudiante+1} es {promedioNotas:.2f}")
    if promedioNotas>=3.0:
        contA=contA+1
    else:
        contP=contP+1

    notaE=promedioNotas+notaE

notaCurso=notaE/numeroEstudiantes

print(f"La nota del curso es {notaCurso}")
print(f"Porcentaje de aprobados {(contA/numeroEstudiantes)*100} %")
print(f"Porcentaje de no aprobados {(contP/numeroEstudiantes)*100} %")
