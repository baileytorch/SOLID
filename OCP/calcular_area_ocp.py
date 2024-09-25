from abc import ABC, abstractmethod

class Forma(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangulo(Forma):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circulo(Forma):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

class CalcularArea:
    def calcular_area(self, forma: Forma):
        return forma.area()
    
        """
        Aquí no es necesario modificar CalcularArea cuando agregamos nuevas formas. 
        Solo extendemos la clase Forma con nuevas subclases que implementen el método area.
        """