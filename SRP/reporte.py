class Reporte:
    def __init__(self, data):
        self.data = data

    def generar_reporte(self):
        return f"Report: {self.data}"

    def guardar_archivo(self, nombrearchivo):
        with open(nombrearchivo, 'w') as file:
            file.write(self.generar_reporte())

        """
        En este caso, la clase Reporte tiene dos responsabilidades: 
        generar el informe y guardar el informe en un archivo. 
        Si la forma de guardar el archivo cambia, también tendría que modificar esta clase.
        """