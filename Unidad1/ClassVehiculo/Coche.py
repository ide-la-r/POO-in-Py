from Vehiculo import Vehiculo

class Coche(Vehiculo):
    def __init__(self, kilometrosRecorridos):
        super().__init__(kilometrosRecorridos)

    def quemar_rueda(self):
        print("¡Estoy quemando rueda con el coche!")

    