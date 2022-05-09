dia= int(input("Ingrese el dd:"))
mes= int(input("Ingrese el mm:"))
año= int(input("Ingrese el yyyy:"))

if dia>=1 and dia<=29:
    dia=dia+1
    print (f"{dia}/{mes}/{año}")
else:
    if dia==30:
        dia=1
        mes=mes+1
        if mes<12:
            mes=mes
        else:
            mes=1
            año=año+1
        print (f"{dia}/{mes}/{año}")
    else:
        print("ingresó una fecha no valida")