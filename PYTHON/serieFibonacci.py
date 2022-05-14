#mathplotlib
def fibonacci(num):
    a=0
    b=1
    c=a+b
    numFibonacci=[a,b,c]
    #num=int(input("Ingrse el número hasta el cual desea calcular la secuencia Fibonacci: "))
    for i in range (2,num):
        a=b
        b=c
        c=a+b
        numFibonacci.append(c)
    print(f"La secuencia Fibonacci hasta el número {num} es: ")
    return numFibonacci

print(fibonacci(15))