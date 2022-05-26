from asyncore import read


f=open("D:/Users/DANIEL/Documents/Downloads/listaMercado.txt","r")
#contenido=f.read()
#print(contenido)
#contenido=f.readline()
#print(contenido)
contenido=f.readlines()
print(contenido)
print(len(contenido))

for vocal in contenido:
    vocal.lower()
    vocalA=vocal.count("a")
    vocalE=vocal.count("e")
    vocalI=vocal.count("i")
    vocalO=vocal.count("o")
    vocalU=vocal.count("u")
    print(f"a:{vocalA}, e:{vocalE}, i:{vocalI}, o:{vocalO}, u:{vocalU}")

f.close()