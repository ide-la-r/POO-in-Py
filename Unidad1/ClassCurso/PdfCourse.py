from POO.Unidad1.ClassCurso.Curso import Curso

class PdfCourse(Curso):
    def __init__(self, titulo, instructor, precio, clases, pages):
        super().__init__(titulo, instructor, precio, clases)
        self.pages = pages


new_course = VideoCourse("Python", "p1", 25, 5, 50)
new_course.show_datails("Python")