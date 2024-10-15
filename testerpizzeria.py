
from maestropizzero import MaestroPizzero
from mozo import Mozo
from pizza import Pizza
from pizzavariedad import PizzaVariedad
from orden import Orden

class TesterPizzeria:
    def __init__(self):
        self.pizzero = MaestroPizzero("Carlos")
        
    def ejecutar(self):
        # Crear variedades de pizza
        variedadMuzzarella = PizzaVariedad("Muzzarella", 800.0)
        variedadNapolitana = PizzaVariedad("Napolitana", 950.5)
        variedadFugazzeta = PizzaVariedad("Fugazzeta", 900.0)
        
        # Crear pizzas usando eas variedades
        pizza1 = Pizza(variedadMuzzarella)
        pizza2 = Pizza(variedadNapolitana)
        pizza3 = Pizza(variedadFugazzeta)
        
        
        # Crear una orden co las pizzas
        orden1 = Orden(1, [pizza1, pizza2, pizza3])
        
        # Cocinar las pizzas
        print("\n Cocinando las pizzas...")
        self.pizzero.cocinar()
        self.imprimirEstadoOrden(orden1)
        
        # Entregar las pizzas
        print("\nEntregando las pizzas...")
        pizzasEntregadas = self.pizzero.entregar(orden1)
        self.imprimirEstadoOrden(orden1)
        
        print("\nPizzas entregadas: ")
        for pizza in pizzasEntregadas:
            print(f"- {pizza.obtenerVariedad().obtenerNombreVariedad()}")
            
    def imprimirEstadoOrden(self, orden: Orden):
        estado_orden = orden.obtenerEstadoOrden()
        estado_str = ""
        if estado_orden == Orden.ESTADO_PARA_ENTREGAR:
            estado_str = "Penddiente de cocinar"
        elif estado_orden == Orden.ESTADO_PARA_ENTREGAR:
            estado_str = "Lista para entregar"
        elif estado_orden == Orden.ESTADO_ENTREGADA:
            estado_str = "Entregada"
            
        print(f"Orden {orden.obtenerEstadoOrden()}: {estado_str}")
        print("Pizzas en la orden:")
        for pizza in orden.obtenerEstadoOrden():
            estado_pizza = pizza.obtenerEstado()
            estado_pizza_str = ""
            if estado_pizza == Pizza.ESTADO_POR_COCINAR:
                estado_pizza_str = "Por cocinar"
            elif estado_pizza == Pizza.ESTADO_COCINADA:
                estado_pizza_str = "cocinada"
            elif estado_pizza == Pizza.ESTADO_ENTREGADA:
                estado_pizza_str = "Entregada"
                
            print(f"- {pizza.obtenerVaridad().obtenerNombreVaridad()}: {estado_pizza_str}")
                
# ejecutar el TestPizzeria
if __name__ == '__main__':
    tester = TesterPizzeria()
    tester.ejecutar()        