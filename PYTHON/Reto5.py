import json
with open("C:/Users/drodriguez/Downloads/paquetes.json") as file:
    empresa = json.load(file)

print((len(empresa['PAQUETES'])))
#print(empresa['PAQUETES']['ALTO'])
print(empresa["PAQUETES"][1]["ALTO"])
#exit()

def calcularCosto(alto,ancho,profundo):
    volumen=alto*ancho*profundo
    if alto<=30:
        costoEnvio=5*volumen
    if alto>30:
        costoEnvio=5*volumen+2000
    if costoEnvio>10000:
        costoEnvio=costoEnvio*1.19
    return costoEnvio

def costoTotal(listaPaquetes,descuento):
    Total=0
    for paquete in range (len(listaPaquetes)):
        alto=empresa["PAQUETES"][paquete]["ALTO"]
        ancho=empresa["PAQUETES"][paquete]["ANCHO"]
        profundo=empresa["PAQUETES"][paquete]["PROFUNDO"]
        Total+=calcularCosto(alto,ancho,profundo)*(1-descuento/100)
    return Total

print (costoTotal(empresa['PAQUETES'], 10))