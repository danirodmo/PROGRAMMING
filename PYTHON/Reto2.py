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
print(volumen)
print(costoEnvio)