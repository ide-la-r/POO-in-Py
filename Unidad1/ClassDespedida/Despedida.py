class Despedida():
    def __init__(self, nombre, hora):
        self.nombre = nombre
        self.hora = hora

    def mostrar_despedida(self):
        if self.hora >= 1 and self.hora < 12 :
            print(f"Que tengas una mañana excelente {self.nombre}")
        elif self.hora >= 12 and self.hora <= 21:
            print(f"Que tengas buena tarde {self.nombre}")
        elif self.hora >= 22 and self.hora <= 24:
            print(f"Que tengas buenas noches {self.nombre}")

    @classmethod
    def desde_texto(cls, texto):
        nombre, hora = texto.split(",")
        return cls(nombre, int(hora))
        
    @staticmethod
    def es_hora_valida(hora):
        return hora > 0 and hora < 24
    

despedida = Despedida("ismael", 23)
despedida.mostrar_despedida()
despedida2 = Despedida.desde_texto("juan,12")
despedida2.mostrar_despedida()
print(despedida.es_hora_valida(despedida.hora))