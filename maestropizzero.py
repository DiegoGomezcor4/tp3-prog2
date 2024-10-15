from orden import Orden
from pizza import Pizza

class MaestroPizzero:

    def __init__(self, nom: str):
        self.__nombre = nom
        self.__ordenes = []

    def establecerNombre(self, nom: str):
        self.__nombre = nom

    def tomarPedido(self, orden: Orden):
        if orden.obtenerEstadoOrden() == orden.ESTADO_INICIAL:
            self.__ordenes.append(orden)

    def cocinar(self):
        for orden in self.__ordenes:
            if orden.obtenerEstadoOrden() == Orden.ESTADO_INICIAL:
                orden.establecerEstadoOrden(Orden.ESTADO_PARA_ENTREGAR)
                for pizza in orden.obtenerPizzas():
                    pizza.establecerEstado(Pizza.ESTADO_COCINADA)

    
    # me quede aca ....
    def entregar(self, pizzas: int):
        pizzasAEntregar = []
        i = 0
        for pizza in self.__pizzasPorEntregar:
            pizzasAEntregar.append(pizza)
            self.__pizzasPorEntregar.remove(pizza)
            i += 1
            if i == pizzas:
                break
        return pizzasAEntregar

    def obtenerNombre(self):
        return self.__nombre
    
    def obtenerPizzasPorCocinar(self):
        return self.__pizzasPorCocinar
    
    def obtenerPizzasPorEntregar(self):
        return self.__pizzasPorEntregar