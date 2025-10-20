class Calificacion():
    def __init__(self, modulo):
        self.modulo = modulo
        self.notaFinal = 0

    def getModulo(self):
        return self.modulo
    
    def getNotaFinal(self):
        return self.notaFinal
    
    def setNotaFinal(self, nota):
        self.notaFinal = nota