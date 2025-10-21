from Vehiculo import Vehiculo

class Bicicleta(Vehiculo):
    def __init__(self, kilometrosRecorridos):
        super().__init__(kilometrosRecorridos)

    def hacer_caballito(self):
        print("¡Estoy haciendo el caballito!")