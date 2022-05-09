a=int(input("Ingrese el primer número: "))
b=int(input("Ingrese el segundo número: "))

while True:
    print("==========MENU==========")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Potenciación")
    opcion=int(input("Ingrese la opción de la operación a realizar: "))
    if opcion==1:
        c=a+b
        print(f"La suma de {a} y {b} es: {c}")
    elif opcion==2:
        c=a-b
        print(f"La resta de {a} y {b} es: {c}")
    elif opcion==3:
        c=a*b
        print(f"La multiplicación de {a} y {b} es: {c}")
    elif opcion==4:
        c=a/b
        print(f"La división de {a} y {b} es: {c}")
    elif opcion==5:
        c=a**b
        print(f"{a} elevado a la {b} es: {c}")
    elif opcion==-1:
        print(f"Gracias por usar el programa. Hasta pronto.")
        break
    else:
        print(f"Por favor digite una opción válida")