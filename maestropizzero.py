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

    
    def entregar(self, orden: Orden):
        if orden.obtenerEstadoOrden() == Orden.ESTADO_PARA_ENTREGAR:
            pizzasAEntregar = []
            for pizza in orden.obtenerPizzas():
                if len(pizzasAEntregar) < 2 and pizza.obtenerEstado() == Pizza.ESTADO_COCINADA:
                    pizza.establecerEstado(Pizza.ESTADO_ENTREGADA)
                    pizzasAEntregar.append(pizza)
                    
            if all(pizza.obtenerEstado() == Pizza.ESTADO_ENTREGADA for pizza in orden.obtenerPizzas()):
                orden.establecerEstadoOrden(Orden.ESTADO_ENTREGADA)
            return pizzasAEntregar

    def obtenerNombre(self):
        return self.__nombre
    
    def obtenerOrdenes(self):
        return self.__ordenes