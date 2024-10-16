from pizza import Pizza

class Mozo:

    # Constructor
    def __init__(self, nom: str):
        self.__nombre = nom # Atributo de instancia: nombre de tipo string
        self.__pizzas = [] # Atributo de instancia: lista de objetos Pizza

    # Comando: establece el nombre del mozo
    def establecerNombre(self, nom: str):
        self.__nombre = nom

    # Comando: toma pizzas
    def tomarPizzas(self, pizzas: list[Pizza]):
        pizzasTomadas = len(self.__pizzas)
        pizzasATomar = len(pizzas)
        if pizzasATomar + pizzasTomadas > 2:
            print(self.__nombre + ": El mozo puede tomar un máximo de 2 pizzas!")
        else:
            for pizza in pizzas:
                print(f"{self.__nombre}: Tomando una pizza de {pizza.obtenerVariedad().obtenerNombreVariedad()}")
                self.__pizzas.append(pizza)
    
    # comando: sirve las pizzas que ha tomado
    def servirPizzas(self):
        for pizza in self.__pizzas:
            
            print(f"- {self.__nombre}  : Sirviendo pizza de   {pizza.obtenerVariedad().obtenerNombreVariedad()}")
        self.__pizzas = [] # Vacia la lista de pizzas una vez servidas
        
    # Consulta: obtiene el nombre del mozo
    def obtenerNombre(self):
        return self.__nombre
    
    # Consulta: obtiene la lista de pizzas
    def obtenerPizzas(self):
        return self.__pizzas
    
    # consulta: devuelve si el mozo puede tomar mas pizzas
    def obtenerEstadoLibre(self):
        pizzasTomadas = len(self.__pizzas)
        return pizzasTomadas < 2