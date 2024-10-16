from maestropizzero import MaestroPizzero
from mozo import Mozo
from orden import Orden
from pizzavariedad import PizzaVariedad
from pizza import Pizza


class TesterPizzeria:

    def main(self):

        # se crean las variedades
        muzza = PizzaVariedad("Muzzarella", 7000.00)
        fugazetta = PizzaVariedad("Fugazetta", 7500.00)
        napolitana = PizzaVariedad("Napolitana", 7500.00)
        rucula = PizzaVariedad("Rucula y Crudo", 9000.00)
        calabresa = PizzaVariedad("Calabresa", 8200.00)
        provolone = PizzaVariedad("Provolone", 8400.00)
        roqueynuez = PizzaVariedad("Roquefort y Nuez", 9000.00)

        # se crean las pizzas
        pizza1 = Pizza(muzza)
        pizza2 = Pizza(fugazetta)
        pizza3 = Pizza(napolitana)
        pizza4 = Pizza(rucula)
        pizza5 = Pizza(calabresa)
        pizza6 = Pizza(provolone)
        pizza7 = Pizza(roqueynuez)
        pizza8 = Pizza(muzza)
        pizza9 = Pizza(fugazetta)
        pizza10 = Pizza(fugazetta)
        pizza11 = Pizza(rucula)
        pizza12 = Pizza(napolitana)
        pizza13 = Pizza(rucula)
        pizza14 = Pizza(provolone)
        pizza15 = Pizza(provolone)
        pizza16 = Pizza(calabresa)

        #se crean las ordenes
        orden1 = Orden(1, [pizza1, pizza10])
        orden2 = Orden(2, [pizza2, pizza11])
        orden3 = Orden(3, [pizza3, pizza12, pizza13])
        orden4 = Orden(4, [pizza4, pizza14])
        orden5 = Orden(5, [pizza5, pizza6, pizza7])
        orden6 = Orden(6, [pizza8, pizza9, pizza15, pizza16])
        ordenes = [orden1, orden2, orden3, orden4, orden5, orden6]
        
        #se crean el maestro pizzero y los mozos
        maestroPizzero = MaestroPizzero("Mario")
        mozo1 = Mozo("Luigi")
        mozo2 = Mozo("Javier")
        
        print("\nestado de todos al inicio")   
        testerPizzeria.imprimirEstadoMaestro(maestroPizzero)
        testerPizzeria.imprimirEstadoMozo(mozo1)
        testerPizzeria.imprimirEstadoMozo(mozo2)

        # maestro pizzero tomam los pedidos
        print('----------------------------------------\nPizzeria de Don Mario\n----------------------------------------')

        print("\nTomando pedidos...")
        for orden in ordenes:
            print("Mario tomando pedido #" + str(orden.obtenerNroOrden()))
            maestroPizzero.tomarPedido(orden)
            
         # estado de todos:
        print("\nestado cuando el maestro pizzero tomo los pedidos")   
        testerPizzeria.imprimirEstadoMaestro(maestroPizzero)
        testerPizzeria.imprimirEstadoMozo(mozo1)
        testerPizzeria.imprimirEstadoMozo(mozo2)
        
        # cocinando las pizzas:
        maestroPizzero.cocinar()

        # entregando pizzas a los mozos:

        mozo1.tomarPizzas(maestroPizzero.entregar(orden1))
        mozo2.tomarPizzas(maestroPizzero.entregar(orden2))
        
        print("\nestado despues de entregar las primeras ordenes")   
        testerPizzeria.imprimirEstadoMaestro(maestroPizzero)
        testerPizzeria.imprimirEstadoMozo(mozo1)
        testerPizzeria.imprimirEstadoMozo(mozo2)
        
        # mozos entregando las ordenes
        mozo1.servirPizzas()
        mozo2.servirPizzas()

        
    
        print("\nestado despues de servir las primeras pizzas")   
        testerPizzeria.imprimirEstadoMaestro(maestroPizzero)
        testerPizzeria.imprimirEstadoMozo(mozo1)
        testerPizzeria.imprimirEstadoMozo(mozo2)

        print("\nmozos tomando las ordenes 3 y 4")
        mozo1.tomarPizzas(maestroPizzero.entregar(orden3))
        mozo2.tomarPizzas(maestroPizzero.entregar(orden4))
        
        
        print("\nestado despues de tomar las ordenes 3 y 4")   
        testerPizzeria.imprimirEstadoMaestro(maestroPizzero)
        testerPizzeria.imprimirEstadoMozo(mozo1)
        testerPizzeria.imprimirEstadoMozo(mozo2)
        
        # sirviendo pizzas de las ordens 3 y 4
        mozo1.servirPizzas()
        mozo2.servirPizzas()
        
        print("\nestado despues de servir pizzas de las ordenes 3 y 4")   
        testerPizzeria.imprimirEstadoMaestro(maestroPizzero)
        testerPizzeria.imprimirEstadoMozo(mozo1)
        testerPizzeria.imprimirEstadoMozo(mozo2)
        
        print("\ncontinuando con la entrega de la orden 3 y 5")
        mozo1.tomarPizzas(maestroPizzero.entregar(orden3))
        mozo2.tomarPizzas(maestroPizzero.entregar(orden5))
        
        print("\nestado despues de tomar las ordenes 3 y 5")   
        testerPizzeria.imprimirEstadoMaestro(maestroPizzero)
        testerPizzeria.imprimirEstadoMozo(mozo1)
        testerPizzeria.imprimirEstadoMozo(mozo2)
        
        mozo1.servirPizzas()
        mozo2.servirPizzas()
        
        print("\nestado despues de servir las ordenes 3 y 5")   
        testerPizzeria.imprimirEstadoMaestro(maestroPizzero)
        testerPizzeria.imprimirEstadoMozo(mozo1)
        testerPizzeria.imprimirEstadoMozo(mozo2)
        

    def imprimirEstadoMaestro(self, maestroPizzero: MaestroPizzero):
        print("\n--------------------------------------------------------------------")
        print(f"Ordenes del Maestro pizzero {maestroPizzero.obtenerNombre()}")
        ordenes = maestroPizzero.obtenerOrdenes() # listado de ordenes
        for orden in ordenes:
            if orden.obtenerEstadoOrden() == 1:
                estado = "ORDEN EN ESTADO INICIAL"
            elif orden.obtenerEstadoOrden() == 2:
                estado = "ORDEN PARA ENTREGAR"
            elif orden.obtenerEstadoOrden() == 3:
                estado = "ORDEN ENTREGADA"
            print(f"Orden numero: {orden.obtenerNroOrden()}, estado: {estado}") # imprime numero de orden
            pizzas = orden.obtenerPizzas()
            for pizza in pizzas:
                variedad = pizza.obtenerVariedad()
                print(f"\t{variedad.obtenerNombreVariedad()}")
        print("--------------------------------------------------------------------\n")

    def imprimirEstadoMozo(self, mozo: Mozo):
        print(f"------------------------Estado del mozo: {mozo.obtenerNombre()}-----------")
        print(f"tienen estas pizzas para entregar!")
        for pizza in mozo.obtenerPizzas():
            print(pizza.obtenerVariedad().obtenerNombreVariedad())

if __name__ == "__main__":
    testerPizzeria = TesterPizzeria()
    testerPizzeria.main()
