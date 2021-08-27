
import menu
import figuras
import signoZodiacal
import numeroE


while True:
    menu.listado()
    opc = int( input("Opción: ") )

    if opc == 1:
        subOpc = figuras.menuFiguras()
        if subOpc == 1:
            figuras.cuadrado()
        elif subOpc ==2:
            figuras.triangulo()
        elif subOpc ==3:
            figuras.circulo()
        menu.pausa()

    elif opc == 2:
        signoZodiacal.menuZodiacal()
        signoZodiacal.calcularZodiacal()
        menu.pausa()

    elif opc == 3:        
        numeroE.calcularNumE()
        menu.pausa()

    elif opc == 4:
        menu.pausa()
        break