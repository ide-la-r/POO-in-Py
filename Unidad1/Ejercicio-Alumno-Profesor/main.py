from Alumno import Alumno
from Profesor import Profesor

alumno1 = Alumno("Ismael", "ism17v2@gmail.com", "1ºDALP", 8.8)
profesor1 = Profesor("Juan", "juancastilla@gmail.com", "IA")

lista1 = [alumno1, profesor1]

for i in lista1:
    i.presentacion()