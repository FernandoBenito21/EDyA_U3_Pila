from Pila import *

if __name__=='__main__':
    decimal=int(input('Ingrese el numero \n'))
    binario = Pila_Encadenada()
    while (decimal > 0):
        resto = decimal % 2
        binario.Insertar(resto)
        decimal = decimal // 2
    print ("El numero en binario es:")
    while (binario.Vacia() == False):
        x = binario.Suprimir()
        print(f"{x}")
    binario.Recorrer()