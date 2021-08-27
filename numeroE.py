from math import factorial

def calcularNumE()->None:
    lim = int( input("Ingresa un numero: ") )
    n = 0 
    e = 0
    for n in range( lim ):
        e+= 1/factorial(n)

    print("El valor de 'e' es: ", e)
    input("")

