class BibliotecaDigital:
    def __init__(self):
        self.__recursos = []

    def aniadir_recurso(self, recurso):
        self.__recursos.append(recurso)
    
    def listar_recursos(self):
        for recurso in self.__recursos:
            print(f"tipo: {recurso.tipo()}, descripcion: {recurso.descripcion_basica()}")

    def abrir_todos(self):
        for recurso in self.__recursos:
            print(recurso.abrir())