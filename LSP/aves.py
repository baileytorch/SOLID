class Ave:
    def volar(self):
        return "Puede Volar"
class Pinguino(Ave):
    def volar(self):
        raise Exception("¡Los pinguinos no pueden volar!")
    
        """
        El pingüino no debería ser una subclase de Ave si no puede volar, porque viola el comportamiento esperado de la clase base.
        """