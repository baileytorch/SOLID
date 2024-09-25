from curses.textpad import rectangle
from turtle import circle


class CalcularArea:
    def calcular_area(self, shape):
        if isinstance(shape, rectangle):
            return shape.width * shape.height
        elif isinstance(shape, circle):
            return 3.14 * shape.radius ** 2
        
        """
        Cada vez que agregas una nueva forma, tienes que modificar la clase CalcularArea.
        """