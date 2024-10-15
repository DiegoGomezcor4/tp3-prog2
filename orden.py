class Orden:
    ESTADO_INICIAL = 1
    ESTADO_PARA_ENTREGAR = 2
    ESTADO_ENTREGADA = 3
    
    # constructor
    def __init__(self, nro: int, pizzas: list):
        self.__nroOrden = nro
        self.__pizzas = pizzas
        self.__estadoOrden = Orden.ESTADO_INICIAL
        
    # comandos
    def establecerNroOrden(self, nro: int):
        self.__nroOrden = nro
        

    def establecerPizzas(self, pizzas: list):
        self.__pizzas = pizzas
        
    def establecerEstadoOrden(self, est: int):
        if est in (Orden.ESTADO_INICIAL, Orden.ESTADO_PARA_ENTREGAR, Orden.ESTADO_ENTREGADA):
           self.__estadoOrden = est 
      
    # consultas:       
    def obtenerNroOrden(self):
        return self.__nroOrden
    
    def obtenerPizzas(self):
        return self.__pizzas
    
    def obtenerEstadoOrden(self):
        return self.__estadoOrden
    
    def calcularTotal(self):
        total = 0.0
        for pizza in self.__pizzas:
            total += pizza.obtenerVariedad().obtenerPrecio()
        return total
    