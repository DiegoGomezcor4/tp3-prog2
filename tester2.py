from maestropizzero import MaestroPizzero
from mozo import Mozo
from pizza import Pizza
from pizzavariedad import PizzaVariedad

# Crear algunas variedades de pizza
muzzarella = PizzaVariedad("Muzzarella", 500.0)
napolitana = PizzaVariedad("Napolitana", 600.0)

# Crear un maestro pizzero
maestro = MaestroPizzero("Mario")

# Crear un mozo
mozo = Mozo("Juan")

# Tomar un pedido
pizza1 = Pizza(muzzarella)
pizza2 = Pizza(napolitana)

# Agregar pizzas a la orden
mozo.tomarPizzas([pizza1, pizza2])

# Servir las pizzas
mozo.servirPizzas()

