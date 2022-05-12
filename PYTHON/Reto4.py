

def calcularCosto(alto,ancho,profundo):
    volumen=alto*ancho*profundo
    if alto<=30:
        costoEnvio=5*volumen
    if alto>30:
        costoEnvio=5*volumen+2000
    if costoEnvio>10000:
        costoEnvio=costoEnvio*1.19
    return costoEnvio

def costoTotal(numeroPaquetes,descuento):
    Total=0
    for paquete in range (numeroPaquetes):
        alto=float(input())
        ancho=float(input())
        profundo=float(input())
        Total=(Total+calcularCosto(alto,ancho,profundo))
    return Total*(1-descuento/100)

print(calcularCosto(35,10,5))
print(costoTotal(2, 50))