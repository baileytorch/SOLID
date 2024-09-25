class Reporte:
    def __init__(self, data):
        self.data = data

    def generar_reporte(self):
        return f"Report: {self.data}"

class GuardarReporte:
    def guardar_archivo(self, reporte, nombrearchivo):
        with open(nombrearchivo, 'w') as file:
            file.write(reporte.generar_reporte())

        """
        Ahora la clase Reporte solo es responsable de generar el informe, 
        y GuardarReporte se encarga de guardar el archivo. 
        Cada clase tiene una única responsabilidad.
        """