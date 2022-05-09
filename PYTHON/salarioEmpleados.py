'''Una empresa tiene un número n de empleados y tiene la siguiente información: cédula, nombre, número de hijos, salario por hora y número de horas trabajadas semanales, la retención por empleado se calcula:
Para salarios menores a 1.300.000: si el número de hijos es mayor a 3 no se le retiene, si el número de hijos es menor o igual a 3 se le retiene un 5% por cada hijo.
Para salarios mayores o iguales a 1.300.000: si el número de hijos es menor a 2, se le retiene un 10%, si es mayor o igual a 2 se le retiene un porcentaje igual a 15 dividido en el número de hijos .
Por cada hijo la empresa le subsidia 20.000.

Elabore un programa que muestre: cédula, nombre del trabajador, salario devengado, retención, subsidio y total a pagar.
'''
numEmpleados=int(input("Digite el número de empleados: "))

for empleado in range (numEmpleados):
    cedula=int(input("Digite el número de la cédula: "))
    nombre=input("Digite el nombre del trabajador: ")
    hijos=int(input("Digite el número de hijos del trabajador: "))
    salarioHora=int(input("Digite el valor del salario en horas: "))
    horasTrabajadas=int(input("Digite la cantidad de horas laboradas: "))
    salarioMensual=salarioHora*horasTrabajadas
    subsidio=hijos*20000
    if salarioMensual<1300000:
        if hijos>3:
            retencion=0
        else:
            retencion=salarioMensual*hijos*0.05
    else:
        if hijos<2:
            retencion=salarioMensual*0.1
        else:
            retencion=salarioMensual*0.15/hijos
    salarioDevengado=salarioMensual+subsidio-retencion
    print(f"-----TRABAJADOR {empleado+1}-----")
    print(f"Cédula: {cedula}")
    print(f"Nombre del trabajador: {nombre}")
    print(f"Salario: ${salarioMensual}")
    print(f"Retención: ${retencion}")
    print(f"Subsidio: ${subsidio}")
    print(f"Total a pagar: ${salarioDevengado}")