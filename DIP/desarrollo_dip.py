from abc import ABC, abstractmethod

class Desarrollador(ABC):
    @abstractmethod
    def desarrollo(self):
        pass

class DesarrolladorBackend(Desarrollador):
    def desarrollo(self):
        return "Codificando en Python"

class DesarrolladorFrontend(Desarrollador):
    def desarrollo(self):
        return "Codificando en JavaScript"

class Proyecto:
    def __init__(self, desarrollador: Desarrollador):
        self.desarrollador = desarrollador

    def desarrollo(self):
        return self.desarrollador.desarrollo()