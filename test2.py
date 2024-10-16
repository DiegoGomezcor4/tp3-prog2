# Supongamos que tienes las clases Pizza, PizzaVariedad, Orden, MaestroPizzero, y Mozo definidas en sus respectivos módulos

from pizza import Pizza
from pizzavariedad import PizzaVariedad
from orden import Orden
from maestropizzero import MaestroPizzero
from mozo import Mozo

def main():
    # Crear variedades de pizzas
    variedad1 = PizzaVariedad("Muzzarella",5000)
    variedad2 = PizzaVariedad("Fugazetta",5500)
    variedad3 = PizzaVariedad("Rucula y Crudo",6000)
    variedad4 = PizzaVariedad("Napolitana",6500)
    variedad5 = PizzaVariedad("Calabresa",7000)

    # Crear pizzas
    pizza1 = Pizza(variedad1)
    pizza2 = Pizza(variedad2)
    pizza3 = Pizza(variedad3)
    pizza4 = Pizza(variedad4)
    pizza5 = Pizza(variedad5)

    # Crear maestro pizzero
    maestroPizzero = MaestroPizzero("Mario")

    # Crear mozos
    mozo1 = Mozo("Luigi")
    mozo2 = Mozo("Javier")

    # Crear ordenes
    orden1= Orden(1,[pizza1,pizza2])
    orden2 = Orden(2,[pizza3,pizza4])
    orden3 = Orden(3,[pizza5])
    

    # Tomar pedidos
    maestroPizzero.tomarPedido(orden1)
    maestroPizzero.tomarPedido(orden2)
    maestroPizzero.tomarPedido(orden3)

    # Mostrar estado de las ordenes
    print("\nOrdenes del Maestro pizzero:")
    for orden in maestroPizzero.obtenerOrdenes():
        print(f"Orden numero: {orden.obtenerNroOrden()} - Estado: {orden.obtenerEstadoOrden()}")

    # Cocinar las ordenes
    maestroPizzero.cocinar()

    # Mostrar estado después de cocinar
    print("\nEstado después de cocinar:")
    for orden in maestroPizzero.obtenerOrdenes():
        print(f"Orden numero: {orden.obtenerNroOrden()} - Estado: {orden.obtenerEstadoOrden()}")
        for pizza in orden.obtenerPizzas():
            print(f"  Pizza: {pizza.obtenerVariedad().obtenerNombreVariedad()} - Estado: {pizza.obtenerEstado()}")

  


    # Los mozos toman las pizzas
    mozo1.tomarPizzas(maestroPizzero.entregar(orden1))
    mozo2.tomarPizzas(maestroPizzero.entregar(orden2))
    mozo1.tomarPizzas(maestroPizzero.entregar(orden3))
    
    # Mostrar estado de los mozos
    print(f"\nEstado de los mozos:")
    print(f"{mozo1.obtenerNombre()} - Pizzas: {[pizza.obtenerVariedad().obtenerNombreVariedad() for pizza in mozo1.obtenerPizzas()]}")
    print(f"{mozo2.obtenerNombre()} - Pizzas: {[pizza.obtenerVariedad().obtenerNombreVariedad() for pizza in mozo2.obtenerPizzas()]}")

    # Los mozos sirven las pizzas
    mozo1.servirPizzas()

    # Mostrar estado final
    print("\nEstado final después de servir las pizzas:")
    print(f"{mozo1.obtenerNombre()} - Pizzas: {[pizza.obtenerVariedad().obtenerNombreVariedad() for pizza in mozo1.obtenerPizzas()]}")
    print(f"{mozo2.obtenerNombre()} - Pizzas: {[pizza.obtenerVariedad().obtenerNombreVariedad() for pizza in mozo2.obtenerPizzas()]}")
    
    # Mostrar estado de las ordenes al final
    print("\nOrdenes del Maestro pizzero:")
    for orden in maestroPizzero.obtenerOrdenes():
        print(f"Orden numero: {orden.obtenerNroOrden()} - Estado: {orden.obtenerEstadoOrden()}")

if __name__ == "__main__":
    main()

