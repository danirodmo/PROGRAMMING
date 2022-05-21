def multiplicarNumeros(numeros):
    mult=1
    for i in numeros:
        mult*=numeros[i]
    return mult

print(multiplicarNumeros([2,3,5]))