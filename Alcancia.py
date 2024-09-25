__author__= "Juan Sebastian Ibarra Salas"
__License__="GPL"
__Version__="1.0.0"
__Email__="juan.ibarrasalas@campusucc.edu.co"

class Alcancia:
    """----------------------------------------------------------------------------------------------
    # Atributos
    ----------------------------------------------------------------------------------------------"""
    
    __Moneda50= 0
    __Moneda100= 0
    __Moneda200= 0
    __Moneda500= 0
    __Moneda1000= 0
    __TotalDinero=0
    
    """#--------------------------------------------------------------------------------------------
    #1=Abierto,#2=Cerrado
    ---------------------------------------------------------------------------------------------#"""
    Estadoalcancia=0
    
    """#--------------------------------------------------------------------------------------------
    # Metodo
    -------------------------------------------------------------------------------------------------#"""
    
    def agregarMoneda50(self,numeroMonedas):
        self.__Monedas50+= numeroMonedas
        self.__TotalDinero += (numeroMonedas*50)
    
    def agregarmoneda500(self,numeroMonedas):
        self.__Monedas500 += numeroMonedas
        self.__TotalDinero += (numeroMonedas*500)
    
    def darTotaldinero (self):
        return self.__TotalDinero
    
    def darNumeroMonedas100 (self):
        return self.__Monedas100
    
    def romperAlcancia (self):
        dinero= self.__Monedas100
        self.__Moneda50=0
        self.__Moneda100= 0
        self.__Moneda200= 0
        self.__Moneda500= 0
        self.__Moneda1000= 0
        self.__TotalDinero=0
        return Dinero
    
    alcancia1 = Alcancia()
    print ("Total dinero al inicio: :", alcancia1.darTotaldinero())