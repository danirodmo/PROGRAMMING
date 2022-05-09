segundos=int(input("Ingrese la cantidad de segundos"))
dias=segundos/86400
decDias=dias%1 #esta operación da los decimales de dias
dd=dias//1 #esta operación da las unidades de dias
horas=decDias*24 #esto da las horas con decimales
decHoras=horas%1 #esto da los decimales de la hora para calcular los minutos
hh=horas//1
minutos=decHoras*60
decMinutos=minutos%1
mm=minutos//1
seg=decMinutos*60
ss=seg//1

print(f"Dias: {dias}")
print(f"decDias: {decDias}")
print(f"dd: {dd}")
print(f"horas: {horas}")
print(f"decHoras: {decHoras}")
print(f"hh: {hh}")
print(f"minutos {minutos}")
print(f"decMinutos {decMinutos}")
print(f"mm {mm}")
print(f"segundos {seg}")
print(f"ss {ss}")

print(f"{segundos} segundos corresponden a {dd} días, {hh} horas, {mm} minutos y {ss} segundos")