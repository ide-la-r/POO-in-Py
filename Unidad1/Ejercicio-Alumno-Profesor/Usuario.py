class Usuario():
    def __init__(self, nombre, email):
        self.__nombre = nombre
        self.__email = email

    def get_nombre(self):
        return self.__nombre

    def get_email(self):
        return self.__email

    def set_nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre

    def set_email(self, nuevo_email):
        self.__email = nuevo_email

    def presentacion(self):
        print(f"Soy {self.__nombre} y mi correo es {self.__email}.")
