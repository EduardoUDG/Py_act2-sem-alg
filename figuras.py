
import math

def menuFiguras()->int:
    print("\n==== ELIGE UNA FIGURA ====")
    print("1) Cuadrado")
    print("2) Triangulo")
    print("3) Circulo")
    opt     = int( input("Opcion: ") )
    return opt 


def cuadrado()->None:
    lado    = float( input("Ingresa el lado del cuadrado: ") )
    print("El area es: ", lado * lado)
    input("")

def triangulo()->None:
    base    = float( input("Ingresa la base del rectangulo: ") )
    altura  = float( input("Ingresa la altura del rectangulo: ") )
    print("El area es: ", (base * altura) / 2)
    input("")

def circulo()->None:
    radio   = float( input("Ingresa el radio del circulo: ") )
    res = math.pi * radio**2
    print("El area es: ", round(res, 2) )
    input("")
