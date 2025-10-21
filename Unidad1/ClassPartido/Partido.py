class Partido():
    def __init__(self, equipo1, equipo2):
        self.equipo1 = equipo1
        self.equipo2 = equipo2

    def anotar_goles(self, goles, equipo):
        equipo.sumar_goles(goles)

    def finalizar_partido(self):
        print(f"Partido finalizado: {self.equipo1.goles} - {self.equipo2.goles}")