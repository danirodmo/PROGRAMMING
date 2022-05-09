nombre=input("Ingrese su nombre")
apellido=input("Ingrese su apellido")
cedula=int(input("Ingrese su cédula"))
correo=input("Ingrese su correo")
salarioMensual=float(input("Ingrese su salario mensual"))
salarioAnual=salarioMensual*13
ultimosDigitos=cedula%100
if salarioAnual>=50831000:
    print("El señor(a)",nombre,apellido,"identificado con cédula de ciudadanía número:",cedula,"debe declarar renta. La información se envía al correo:",correo)
    if ultimosDigitos%100>=0 and ultimosDigitos%100<=20:
        print("Su plazo máximo para declarar es agosto 10")
    if ultimosDigitos%100>21 and ultimosDigitos%100<=40:
        print("Su plazo máximo para declarar es agosto 20")
    if ultimosDigitos%100>41 and ultimosDigitos%100<=60:
        print("Su plazo máximo para declarar es agosto 30")
    if ultimosDigitos%100>61 and ultimosDigitos%100<=80:
        print("Su plazo máximo para declarar es septiembre 10")
    if ultimosDigitos%100>81 and ultimosDigitos%100<=99:
        print("Su plazo máximo para declarar es septiembre 20")
else:
    print("El señor(a)",nombre,apellido,"identificado con cédula de ciudadanía número:",cedula,"no debe declarar renta. La información se envía al correo:",correo)