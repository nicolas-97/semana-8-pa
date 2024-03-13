class Configuracion:
    _instancia = None

    def __new__(cls, *args, **kwargs):
        if cls._instancia is None:
            cls._instancia = super().__new__(cls, *args, **kwargs)
        return cls._instancia

    def __init__(self):
        self.opcion1 = "valor1"
        self.opcion2 = "valor2"

# Uso del Singleton
configuracion = Configuracion()
configuracion_dos = Configuracion()

print(configuracion, configuracion_dos)

print(configuracion is configuracion_dos)

print(configuracion == configuracion_dos)