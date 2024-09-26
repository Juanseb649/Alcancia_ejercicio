__author__= "Juan Sebastian Ibarra Salas"
__License__="GPL"
__Version__="1.0.0"
__Email__="juan.ibarrasalas@campusucc.edu.co"

class Alcancia:
    """----------------------------------------------------------------------------------------------
    # Atributos
    ----------------------------------------------------------------------------------------------"""
    __Moneda50 = 0
    __Moneda100 = 0
    __Moneda200 = 0
    __Moneda500 = 0
    __Moneda1000 = 0
    __TotalDinero = 0
    
    """#--------------------------------------------------------------------------------------------
    #1=Abierto,#2=Cerrado
    ---------------------------------------------------------------------------------------------#"""
    EstadoAlcancia = 0
    
    """#--------------------------------------------------------------------------------------------
    # Metodo
    -------------------------------------------------------------------------------------------------#"""
    __method__ = "constructor"
    __parameter__= "Moneda50, Moneda100, Moneda200, Moneda500, Moneda1000"
    __return__="ninguna"
    __description__="Metodo constructor de la clase"
    def __init__(self, Moneda50, Moneda100, Moneda200, Moneda500, Moneda1000):
        self.Moneda50 = Moneda50
        self.Moneda100 = Moneda100
        self.Moneda200 = Moneda200
        self.Moneda500 = Moneda500
        self.Moneda1000 = Moneda1000
        
        self.agregarMoneda50(Moneda50)
        self.agregarMoneda100(Moneda100)
        self.agregarMoneda200(Moneda200)
        self.agregarMoneda500(Moneda500)
        self.agregarMoneda1000(Moneda1000)
        
    def agregarMoneda50(self, numeroMonedas):
        self.__Moneda50 += numeroMonedas
        self.__TotalDinero += (numeroMonedas * 50)
    
    def agregarMoneda100(self, numeroMonedas):
        self.__Moneda100 += numeroMonedas
        self.__TotalDinero += (numeroMonedas * 100)
    
    def agregarMoneda200(self, numeroMonedas):
        self.__Moneda200 += numeroMonedas
        self.__TotalDinero += (numeroMonedas * 200)
    
    def agregarMoneda500(self, numeroMonedas):
        self.__Moneda500 += numeroMonedas
        self.__TotalDinero += (numeroMonedas * 500)
        
    def agregarMoneda1000(self, numeroMonedas):
        self.__Moneda1000 += numeroMonedas
        self.__TotalDinero += (numeroMonedas * 1000)
    
    def darTotalDinero (self):
        return self.__TotalDinero
    
    def darNumeroMonedas100 (self):
        return self.__Moneda100
    
    def romperAlcancia (self):
        dinero= self.__Moneda100
        self.__Moneda50 = 0
        self.__Moneda100 = 0
        self.__Moneda200 = 0
        self.__Moneda500 = 0
        self.__Moneda1000 = 0
        self.__TotalDinero = 0
        
        return dinero
    
Alcancia1 = Alcancia(1, 2, 3, 4, 100)
print ("Total monedas de 50:", Alcancia1.Moneda50)
print ("Total monedas de 100:", Alcancia1.Moneda100)
print ("Total monedas de 200:", Alcancia1.Moneda200)
print ("Total monedas de 500:", Alcancia1.Moneda500)
print ("Total monedas de 1000:", Alcancia1.Moneda1000)
print ("Total dinero al inicio:", Alcancia1.darTotalDinero())