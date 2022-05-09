partidosGanados=int(input("Ingrese la cantidad de partidos ganados: "))
partidosEmpatados=int(input("Ingrese la cantidad de partidos empatados: "))
partidosPerdidos=int(input("Ingrese la cantidad de partidos perdidos: "))
PuntosTotales=3*partidosGanados+partidosEmpatados
print(f"Los puntos totales son: {PuntosTotales}")