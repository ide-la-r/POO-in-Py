class Punto():
    def __init__(self, x, y, constante):
        self.x = x
        self.y = y
        self.constante = constante

    def __str__(self):
        return f"{self.x}, {self.y}, {self.constante}"

p1 = Punto(4,4,1)
print(p1.__str__())