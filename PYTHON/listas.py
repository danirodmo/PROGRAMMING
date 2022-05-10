from numeroPerfectoFunction import numPerfect

miLista=[1,2,3,"Daniel",3]
miLista.append("Luisa")
print(miLista)
miLista.clear()
print(miLista)
miLista=[1,2,3,"Daniel",3]
contador=miLista.count(3)
print(contador)
miLista.insert(2,"Baby")
print(miLista)
miLista[3]="Mayotta"
print(miLista)
miLista.pop(0)
print(miLista)

numPerfect()