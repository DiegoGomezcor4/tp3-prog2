class PizzaVariedad:
    def __init__(self, nomVar: str, pre: float):
        if pre > 0.0:
            self.__nombreVariedad = nomVar
            self.__precio = pre
            
    def establecerNombreVariedad(self, nomVar: str):
        self.__nombreVaridad = nomVar
        
    
    def establecerPrecio(self, pre: float):
        if pre > 0.0:
            self.__precio = pre
            
    def obtenerNombreVariedad(self):
        return self.__nombreVaridad
    
    def obtenerPrecio(self):
        return self.__precio
    
    