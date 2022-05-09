from math import sqrt


a=float(input("Ingrese el término a: "))
b=float(input("Ingrese el término b: "))
c=float(input("Ingrese el término c: "))

discriminante=b**2-4*a*c

if discriminante<0:
    print("No hay solución real, por favor ingrese otros valores")
else:
    raiz1=(-b+sqrt(b**2-4*a*c))/(2*a)
    raiz2=(-b-sqrt(b**2-4*a*c))/(2*a)
    print(f"La primera raíz es {raiz1:.2f}")
    print(f"La segunda raíz es {raiz2:.2f}")