from Persona import Persona

class Alumno(Persona):
    def __init__(self, dni, nombre, apellidos, fechaNacimiento, ciclo):
        super().__init__(dni, nombre, apellidos, fechaNacimiento)
        self.ciclo = ciclo
        self.calificacion = []

    def matricular(self, modulo):
        pass

    def calificar(self, modulo, nota):
        pass

    def promociona(self):
        return True
    
    def getNotaMedia(self):
        pass

    def toString(self):
        pass