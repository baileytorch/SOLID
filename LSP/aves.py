from abc import ABC, abstractmethod
""" Clase en la que se pueden definir tanto métodos como propiedades, pero que no pueden ser instancias directamente. 
Solamente se pueden usar para construir subclases. """

class Ave(ABC):
    def __init__(self, nombre):
        self.nombre = nombre
    
    @abstractmethod
    def volar(self):
        pass

    @abstractmethod
    def nadar(self):
        pass

    @abstractmethod
    def hacer_sonido(self) -> str:
        pass

class Cuervo(Ave):
    def volar(self):
        print(f"!Vuela alto {self.nombre}!")

    def nadar(self):
        raise NotImplementedError("Crows don't swim!")

    def do_sound(self) -> str:
        return "Caw"

class Pato(Ave):   
    def volar(self):
        print(f"{self.nombre} no puede volar muy alto...")

    def nadar(self):
        print(f"{self.nombre} nada en el lago")

    def hacer_sonido(self) -> str:
        return "Quack!"