from RecursoDigital import RecursoDigital

class VideoCurso(RecursoDigital):
    def __init__(self, titulo, autor, anio, duracion_minutos, nivel):
        super().__init__(titulo, autor, anio)
        self.duracion_minutos = duracion_minutos
        self.nivel = nivel

    def abrir(self):
        return f"Abriendo Video {self.get_titulo()}, de nivel {self.nivel}"
    
    def tipo(self):
        return f"Video"