notasPython=[["Daniel","Rodríguez",4.5],["Jason","Roa",5],["Bibiana","Gonzalez",4.8]]
print(notasPython[1][2])
suma=0
for i in range (len(notasPython)):
    suma+=notasPython[i][2]
    promedio=suma/len(notasPython)
print(promedio)