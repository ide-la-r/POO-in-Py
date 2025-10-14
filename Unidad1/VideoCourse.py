from Curso import Curso

class VideoCourse(Curso):
    def __init__(self, titulo, instructor, precio, clases, length_video):
        super().__init__(titulo, instructor, precio, clases)
        self.length_video = length_video


new_course = VideoCourse("Python", "p1", 25, 5, 50)
new_course.show_datails("Python")