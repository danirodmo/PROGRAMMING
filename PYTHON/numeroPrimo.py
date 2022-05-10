def primo (numero):
    divisor=0
    for i in range (numero+1):
        if numero%i==0:
            divisor=divisor+1
            