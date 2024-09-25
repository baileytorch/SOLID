class DesarrolladorBackend:
    def desarrollo(self):
        return "Codificando en Python"

class Proyecto:
    def __init__(self):
        self.backend = DesarrolladorBackend()

    def develop(self):
        return self.backend.desarrollo()
    
        """
        Aquí, la clase Proyecto depende directamente de DesarrolladorBackend.
        Si quisiéramos cambiar el desarrollador a otro que use JavaScript, tendríamos que modificar Proyecto.
        """