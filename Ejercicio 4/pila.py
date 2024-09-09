class Nodo:
    def __init__(self):
        __item = 0
        __sig = None

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
            self.__cabeza= None
            self.__cant=0
        
        def Vacia(self):
            return self.__cabeza == None
        
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
                self.__cant -= 1
                retorna = x.getItem()
            return retorna
        
        def Recorrer(self):
            x = self.__cabeza
            while (x != None):
                print("{}".format(x.getItem()))
                x = x.getSig()
            return None
