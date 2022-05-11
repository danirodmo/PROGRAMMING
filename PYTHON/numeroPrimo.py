from Ejercicio2 import convTemp
def primo ():
    numero=int(input("Ingrese un número entero: "))
    for numero in range (1,numero+1):
        divisor=0
        for i in range (1,numero+1):
            if numero%i==0:
                divisor=divisor+1
        if divisor==2:
            print(f"{numero} es número primo")
        else:
            print(f"{numero} no es número primo")

primo()
convTemp()