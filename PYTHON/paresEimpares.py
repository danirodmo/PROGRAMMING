suma=0
mult=1
for number in range(1,21):
    if number%2==0:
        suma=number+suma
    else:
        mult=number*mult
print(f"La suma de los números pares es: {suma}")
print(f"La multiplicación de los números impares es: {mult}")