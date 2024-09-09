from Pila import *

if __name__ =='__main__':
    numero = int (input('Ingrese el numero para obtener su factorial:'))
    operandos = Pila_Encadenada()
    if (numero == 0):
        operandos.Insertar(1)
    else:
        while (numero > 0):
            operandos.Insertar(numero)
            numero -= 1
    operandos.Recorrer()
    fact = 1
    while (operandos.Vacia() == False):
        x = operandos.Suprimir()
        fact = fact * x
    print(f"El factorial del numero ingresado es:{fact}")
    