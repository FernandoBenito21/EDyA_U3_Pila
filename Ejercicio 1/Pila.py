import numpy as np

class Pila_Secuecial:
    __tope = 0
    __cantidad = 0
    __dimension = 0
    __arreglo = None
    
    def __init__(self, dimension):
        self.__arreglo = np.empty(dimension, dtype=int)
        self.__tope = 0
        self.__dimension = dimension
    
    def Vacia (self):
        return (self.__tope == 0)
    
    def Insertar(self, x):
        if (self.__cantidad >= self.__dimension):
            self.__arreglo[self.__tope] = x
            self.__tope += 1
            self.__cantidad += 1
        else:
            print ("La pila está llena \n")
        return self.__arreglo

    def Suprimir(self):
        retorna: None
        if (self.Vacia() == True):
            print ("La pila está vacia \n")
        else:
            x=self.__arreglo[self.__tope-1]
            self.__tope -= 1
            retorna = x
        return retorna
    
    def Recorrer(self):
        if self.Vacia() == False:
            i = self.tope-1
            while (i>=0):
                print ("{}".format(self.__arreglo[i]))
                i -= 1
        else:
            print ("La pila está vacía \n")

class Nodo:
    def __init__(self):
        self.__item = 0
        self.__sig = None

    def getItem(self):
        return self.__item

    def cargaItem(self, unItem):
        self.__item= unItem

    def cargaSig(self, tope):
        self.__sig= tope

    def getSig(self):
        return self.__sig

class Pila_Encadenada:
        __cabeza : Nodo
        def __init__(self):
            self.__cabeza = None
            self.__cant=0
        
        def Vacia(self):
            return self.__cant == 0
        
        def Insertar(self, x):
            Elemento = Nodo()
            Elemento.cargaItem(x)
            Elemento.cargaSig(self.__cabeza)
            self.__cabeza = Elemento
            self.__cant += 1
        
        def Suprimir(self):
            retorna = None
            if self.Vacia() == False:
                x = self.__cabeza
                self.__cabeza = self.__cabeza.getSig()
                retorna = x
            else:
                print ("La pila esta vacia \n")
            return retorna
        
        def Recorrer(self):
            x = self.__cabeza
            while (x != None):
                print("{}".format(x.getItem()))
                x = x.getSig()
            return None