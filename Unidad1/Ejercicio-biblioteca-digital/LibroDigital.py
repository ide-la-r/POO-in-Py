from RecursoDigital import RecursoDigital

class LibroDigital(RecursoDigital):
    def __init__(self, titulo, autor, anio, num_paginas, formato):
        super().__init__(titulo, autor, anio)
        self.num_paginas = num_paginas
        self.formato = formato

    def abrir(self):
        return f"Abriendo libro {self.get_titulo()}, en formato {self.formato}"
    
    def tipo(self):
        return f"Libro"