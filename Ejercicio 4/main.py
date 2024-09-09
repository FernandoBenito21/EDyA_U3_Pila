from pila import *
"""el numero minimo de jugadas es (2**n)-1"""

'''def Primer_Carga(cant, pila):
    x=0
    while(x <= cant):
        pila.Insertar(cant)
        cant -= 1
        x += 1
    return None'''


if __name__=='__main__':
    pila_1 = Pila_Encadenada()
    pila_2 = Pila_Encadenada()
    pila_3 = Pila_Encadenada()
    cant_fichas = int(input('Ingresar la cantidad de fichas para jugar:'))
    '''primer carga'''
    x=1
    cant=cant_fichas
    while(x <= cant_fichas):
        pila_1.Insertar(cant)
        cant -= 1
        x += 1
    print("pila 1:")
    pila_1.Recorrer()
    print("pila 2:")
    pila_2.Recorrer()
    print("pila 3:")
    pila_3.Recorrer()
    '''empieza el juego'''
    movimientos = 0
    cant = 0
    while (cant != cant_fichas):
        origen = int(input('Ingrese la pila origen:'))
        destino = int(input('Ingrese la pila destino:'))
        if (origen == 1):
            if (destino == 2):
                if (pila_1.Vacia() == False):
                    if (pila_2.Vacia() == False):
                        a = pila_1.Suprimir()
                        b = pila_2.Suprimir()
                        if (a < b):
                            pila_2.Insertar(b)
                            pila_2.Insertar(a)
                        else:
                            pila_1.Insertar(a)
                            pila_2.Insertar(b)
                            print("No se pueden colocar fichas de valor superior sobre fichas de valor inferior \n")
                    else:
                        a = pila_1.Suprimir()
                        pila_2.Insertar(a)
                else:
                    print("La pila origen no tiene fichas \n")
            elif (destino == 3):
                if (pila_1.Vacia() == False):
                    if (pila_3.Vacia() == False):
                        a = pila_1.Suprimir()
                        b = pila_3.Suprimir()
                        if (a < b):
                            pila_3.Insertar(b)
                            pila_3.Insertar(a)
                            cant += 1
                        else:
                            pila_1.Insertar(a)
                            pila_3.Insertar(b)
                            print("No se pueden colocar fichas de valor superior sobre fichas de valor inferior \n")
                    else:
                        a = pila_1.Suprimir()
                        pila_3.Insertar(a)
                        cant += 1
                else:
                    print("La pila origen no tiene fichas \n")
        elif (origen == 2):
            if (destino == 1):
                if (pila_2.Vacia() == False):
                    if (pila_1.Vacia() == False):
                        a = pila_2.Suprimir()
                        b = pila_1.Suprimir()
                        if (a < b):
                            pila_1.Insertar(b)
                            pila_1.Insertar(a)
                        else:
                            pila_2.Insertar(a)
                            pila_1.Insertar(b)
                            print("No se pueden colocar fichas de valor superior sobre fichas de valor inferior \n")
                    else:
                        a = pila_2.Suprimir()
                        pila_1.Insertar(a)
                else:
                    print("La pila origen no tiene fichas \n")
            elif (destino == 3):
                if (pila_2.Vacia() == False):
                    if (pila_3.Vacia() == False):
                        a = pila_2.Suprimir()
                        b = pila_3.Suprimir()
                        if (a < b):
                            pila_3.Insertar(b)
                            pila_3.Insertar(a)
                            cant += 1
                        else:
                            pila_2.Insertar(a)
                            pila_3.Insertar(b)
                            print("No se pueden colocar fichas de valor superior sobre fichas de valor inferior \n")
                    else:
                        a = pila_2.Suprimir()
                        pila_3.Insertar(a)
                        cant += 1
                else:
                    print("La pila origen no tiene fichas \n")
        if (origen == 3):
            if (destino == 1):
                if (pila_3.Vacia() == False):
                    if (pila_1.Vacia() == False):
                        a = pila_3.Suprimir()
                        b = pila_1.Suprimir()
                        if (a < b):
                            pila_1.Insertar(b)
                            pila_1.Insertar(a)
                            cant -= 1
                        else:
                            pila_3.Insertar(a)
                            pila_1.Insertar(b)
                            print("No se pueden colocar fichas de valor superior sobre fichas de valor inferior \n")
                    else:
                        a = pila_3.Suprimir()
                        pila_1.Insertar(a)
                        cant -= 1
                else:
                    print("La pila origen no tiene fichas \n")
            elif (destino == 2):
                if (pila_3.Vacia() == False):
                    if (pila_2.Vacia() == False):
                        a = pila_3.Suprimir()
                        b = pila_2.Suprimir()
                        if (a < b):
                            pila_2.Insertar(b)
                            pila_2.Insertar(a)
                            cant -= 1
                        else:
                            pila_3.Insertar(a)
                            pila_2.Insertar(b)
                            print("No se pueden colocar fichas de valor superior sobre fichas de valor inferior \n")
                    else:
                        a = pila_3.Suprimir()
                        pila_2.Insertar(a)
                        cant -= 1
                else:
                    print("La pila origen no tiene fichas \n")
        movimientos += 1
        print("pila 1:")
        pila_1.Recorrer()
        print("pila 2:")
        pila_2.Recorrer()
        print("pila 3:")
        pila_3.Recorrer()
    minimos = (2**cant_fichas) -1
    print ("La partida ha finalizado, tus estadisticas finales son: \n")
    print (f"movimientos realizados: {movimientos} \n")
    print (f"movimientos minimos posibles: {minimos}")