
def convTemp ():
    t=input("Seleccione 'F' para convertir de grados Fahrenheit a grados Celsius, o 'C' para convertir de grados Celsius a Fahrenheit: ").upper()
    if t=="F":
        F=float(input("Ingrese la temperatura en grados Fahrenheit: "))
        C=(F-32)/1.8
        print(f"La temperatura en grados Celsius es: {C:.1f}")
    elif t=="C":
        C=float(input("Ingrese la temperatura en grados Celsius: "))
        F=1.8*C+32
        print(f"La temperatura en grados Fahrenheit es: {F:.1f}")
    else:
        print("Selección incorrecta. Hasta luego".upper())
        
convTemp()