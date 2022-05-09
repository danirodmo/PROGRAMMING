realPassword= "Daniel"

contador=0
while contador <3:
    contador=contador+1
    password=input("Ingrese la contraseña: ")
    if password==realPassword:
        print("Bienvenido")
        break
    else:
        print("Intente de nuevo, contraseña incorrecta")
        print(f"Quedan {3-contador} intentos")
        if contador==3:
            print("Ha utilizado sus 3 intentos")
