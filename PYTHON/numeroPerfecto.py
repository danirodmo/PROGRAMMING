numero=int(input("Ingrese un número: "))
sumaDivisores=0
for i in range (1,numero):
    if numero%i==0:
        sumaDivisores=i+sumaDivisores
        print(f"Sus divisores son: {i}")
print(sumaDivisores)
if sumaDivisores==numero:
    print(f"{numero} es número perfecto")
else:
    print(f"{numero} no es número perfecto")