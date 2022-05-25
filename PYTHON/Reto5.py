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
        costoEnvio*=1.19
    return costoEnvio

def costoTotal(listaPaquetes,descuento):
    Total=0
    for paquete in listaPaquetes:
        alto=paquete['ALTO']
        ancho=paquete['ANCHO']
        profundo=paquete['PROFUNDO']
        Total+=calcularCosto(alto,ancho,profundo)
    return Total*(1-descuento/100)

print (costoTotal(empresa['PAQUETES'], 10))


exit()
print (costoTotal(paquetes, 0))
paquetes = [
  {
    'ALTO': 20,
    'ANCHO': 10,
    'PROFUNDO': 5
  },
  {
    'ALTO': 7,
    'ANCHO': 10,
    'PROFUNDO': 5
  },
]
print (costoTotal(paquetes, 10))
paquetes = [
  {
    'ALTO': 20,
    'ANCHO': 10,
    'PROFUNDO': 5
  },
  {
    'ALTO': 7,
    'ANCHO': 10,
    'PROFUNDO': 5
  },
]
print (costoTotal(paquetes, 15))
25585.0
6075.0
5737.5

