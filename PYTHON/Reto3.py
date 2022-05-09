numPaquetes=int(input())
costoTotal=0

for paquete in range (numPaquetes):
    alto=float(input())
    ancho=float(input())
    profundo=float(input())
    volumen=alto*ancho*profundo
    if alto<=30:
        costoEnvio=5*volumen
    if alto>30:
        costoEnvio=5*volumen+2000
    if costoEnvio>10000:
        costoEnvio=costoEnvio*1.19
    costoTotal=costoTotal+costoEnvio
    print("volumen: ",volumen)
    print("costo envio: ",costoEnvio)
print("costo total: ",costoTotal)