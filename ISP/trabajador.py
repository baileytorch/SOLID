class InterfazTrabajador:
    def trabajar(self):
        pass

    def comer(self):
        pass

class Robot(InterfazTrabajador):
    def trabajar(self):
        print("Robot está trabajando")

    def comer(self):
        raise NotImplementedError("Los robots no comen")
    
        """
        Aquí la interfaz InterfazTrabajador tiene un método eat que no tiene sentido para Robot.
        """