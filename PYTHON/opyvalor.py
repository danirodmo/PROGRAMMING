valor=int(input("Ingrese un valor"))
op=int(input("Ingrese un operador"))

if op==1:
    resultado=100*valor
    print(f"El resultado con el operador {op} es {resultado}")
elif op==2:
    resultado=100**valor
    print(f"El resultado con el operador {op} es {resultado}")
elif op==3:
    resultado=100/valor
    print(f"El resultado con el operador {op} es {resultado}")
else:
    resultado=0
    print(f"El resultado con el operador {op} es {resultado}")