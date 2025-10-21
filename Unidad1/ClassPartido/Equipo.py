class Equipo:
    def __init__(self, nombre, jugadores=None, goles=0):
        self.nombre = nombre
        if jugadores is None:
            jugadores = []
        self.jugadores = jugadores
        self.goles = goles

    def aniadir_jugadores(self, jugador):
        if len(self.jugadores) < 4:
            self.jugadores.append(jugador)
            print(f"Jugador {jugador.nombre} añadido correctamente")
        else:
            print("Ha habido un error creando el jugador")

    def sumar_goles(self, goles):
        self.goles += goles
