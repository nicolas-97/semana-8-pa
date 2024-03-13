class Configuracion:
    _instancia = None

    def __init__(self):
        if Configuracion._instancia is not None:
            raise Exception("Esta clase es un singleton, no se puede instanciar más de una vez.")
        else:
            self.opcion1 = "valor1"
            self.opcion2 = "valor2"
            Configuracion._instancia = self

    @staticmethod
    def obtener_instancia():
        if Configuracion._instancia is None:
            Configuracion._instancia = Configuracion()
        return Configuracion._instancia


configuracion = Configuracion.obtener_instancia()
configuracion_dos = Configuracion.obtener_instancia()

print(configuracion)
print(configuracion_dos)
