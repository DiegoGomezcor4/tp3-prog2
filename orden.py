class Orden:
    ESTADO_INICIAL = 1
    ESTADO_PARA_ENTREGAR = 2
    ESTADO_ENTREGADA = 3
    
    def __init__(self, nro: int, pizzas: list):
        self.__nroOrden = nro
        self.__pizzas = pizzas
        self.__estadoOrden = Orden.ESTADO_INICIAL
        
    
    def establecerNroOrden(self, nro: int):
        self.__nroOrden = nro
        

    def establecerPizzas(self, pizzas: list):
        self.__pizzas = pizzas
        
    def establecerEstadoOrden(self, est: int):
        if est in (Orden.ESTADO_INICIAL, Orden.ESTADO_PARA_ENTREGAR, Orden.ESTADO_ENTREGADA):
           self.__estadoOrden = est 
    