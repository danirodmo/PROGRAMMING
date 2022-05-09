n = int(input("Ingrese el número de filas: "))
caracter = input("Ingrese el caracter a representar: ")
for i in range (n):
    print((i+1)*caracter)
for i in range (n,0,-1):
    print((i-1)*caracter)