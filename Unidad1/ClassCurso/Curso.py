from statistics import mean

class Curso:
    usuarios = []
    calificaciones = []
    calificacion_promedio = 0.0

    def __init__(self, titulo, instructor, precio, clases):
        self.titulo = titulo
        self.instructor = instructor
        self.precio = precio
        self.clases = clases
    
    def new_user_enrolled(self, name):
        Curso.usuarios.append(name)

    def received_a_rating(self, rating):
        Curso.calificaciones.append(rating)
        Curso.calificacion_promedio = mean(Curso.calificaciones)

    def show_datails(self, titulo):
        if self.titulo == titulo:
            print(self.__str__())

    def __str__(self):
        return f"{self.titulo}, {self.instructor}, {self.precio}, {self.clases}"
    

