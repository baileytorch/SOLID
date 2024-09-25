from abc import ABC, abstractmethod

class Trabajo(ABC):
    @abstractmethod
    def trabajar(self):
        pass

class Comida(ABC):
    @abstractmethod
    def comer(self):
        pass

class Humano(Trabajo, Comida):
    def trabajar(self):
        print("El humano está trabajando")

    def comer(self):
        print("El humano está comiendo")

class Robot(Trabajo):
    def trabajar(self):
        print("El robot está trabajando")
        
        """
        Aquí dividimos la interfaz en dos: Trabajo y Comida, 
        lo que permite que Robot solo implemente lo que necesita (trabajar), 
        sin tener que manejar métodos innecesarios como comer.
        """