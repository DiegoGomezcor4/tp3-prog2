# tester_amplio.py

from pizzavariedad import PizzaVariedad
from pizza import Pizza
from mozo import Mozo
from maestropizzero import MaestroPizzero

def main():
    # Crear variedades de pizza
    muzzarella = PizzaVariedad("Muzzarella", 500)
    napolitana = PizzaVariedad("Napolitana", 600)
    cuatro_quesos = PizzaVariedad("Cuatro Quesos", 700)
    fugazzeta = PizzaVariedad("Fugazzeta", 650)

    # Crear pizzas
    pizza1 = Pizza(muzzarella)
    pizza2 = Pizza(napolitana)
    pizza3 = Pizza(cuatro_quesos)
    pizza4 = Pizza(fugazzeta)

    # Crear un mozo
    mozo = Mozo("Juan")

    # Probar tomar pizzas
    print("\n--- Tomando Pizzas ---")
    mozo.tomarPizzas([pizza1, pizza2])
    print(f"{mozo.obtenerNombre()} ha tomado las pizzas: {[pizza.obtenerVariedad().nombre for pizza in mozo.obtenerPizzas()]}")

    # Intentar tomar más pizzas de las que puede llevar
    print("\n--- Intentando tomar más pizzas ---")
    mozo.tomarPizzas([pizza3, pizza4])  # Debería dar un mensaje de error

    # Servir pizzas
    print("\n--- Sirviendo Pizzas ---")
    mozo.servirPizzas()

    # Mostrar estado del mozo después de servir
    print(f"{mozo.obtenerNombre()} tiene {len(mozo.obtenerPizzas())} pizzas después de servir.")

    # Crear un maestro pizzero
    maestro = MaestroPizzero("Carlos")

    # Simular un pedido
    print("\n--- Maestro Pizzero tomando pedidos ---")
    maestro.tomarPedido(pizza1)  # Tomando pedido de una pizza
    maestro.tomarPedido(pizza3)  # Tomando pedido de otra pizza

    # Cocinar y entregar
    print("\n--- Cocinando y entregando pizzas ---")
    maestro.cocinar()  # Debería cocinar las pizzas
    maestro.entregar()  # Debería entregar las pizzas

if __name__ == "__main__":
    main()
