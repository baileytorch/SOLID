class Ave:
    def moverse(self):
        return "Moviéndose"

class Gorrion(Ave):
    def moverse(self):
        return "Volando"

class Pinguino(Ave):
    def moverse(self):
        return "Nadando"
    
        """En este caso, Pinguino y Gorrion son subclases de Ave, 
        pero ambas cumplen con el comportamiento general de "moverse" sin romper la funcionalidad de la clase base.
        """