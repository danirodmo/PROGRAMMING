n = int(input("Ingrese el número de filas: "))
caracter = input("Ingrese el caracter a representar: ")
for i in range (1,n+1):
    if i==1:
        print(caracter*n*2)
    elif i>=2 and i<n:
        print(caracter*2+" "*(n*2-4)+caracter*2)
    else:
        print(caracter*n*2)