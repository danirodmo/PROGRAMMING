#numero=0 #para trabajar con while
for numero in range(1000+1):
    #numero=int(input("Ingrese un número: ")) pidiendo que se pregunta el numero
    sumaDivisores=0
    for i in range (1,numero):
        if numero%i==0:
            sumaDivisores=i+sumaDivisores
    
    if sumaDivisores==numero:
        print(f"{numero} es número perfecto")
        
    else:
        print(f"{numero} no es número perfecto")
    #numero=numero+1 #para trabajar con while