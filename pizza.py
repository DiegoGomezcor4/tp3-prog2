from pizzavariedad import PizzaVariedad
class Pizza:
    
    ESTADO_POR_COCINAR = 1
    ESTADO_COCINADA = 2
    ESTADO_ENTREGADA = 3

    def __init__(self, var: PizzaVariedad):
        self.__variedad = var
        self.__estado = Pizza.ESTADO_POR_COCINAR

    def establecerVariedad(self, var: PizzaVariedad):
        self.__variedad = var
        
    def establecerEstado(self, est: int):
        if est in (Pizza.ESTADO_POR_COCINAR, Pizza.ESTADO_POR_COCINAR, Pizza.ESTADO_ENTREGADA):
            self.__estado = est

    def obtenerVariedad(self):
        return self.__variedad
    
    def obtenerEstado(self):
        return self.__estado