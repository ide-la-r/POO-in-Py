class Vehiculo():
    vehiculosCreados = 0
    kilometrosTotales = 0
    def __init__(self, kilometrosRecorridos):
        self.kilometrosRecorridos = kilometrosRecorridos
        Vehiculo.vehiculosCreados += 1        

    def anda(self, km):
        self.kilometrosRecorridos += km
        Vehiculo.kilometrosTotales += km