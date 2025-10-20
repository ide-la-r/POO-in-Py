class Persona():
    def __init__(self, dni, nombre, apellidos, fechaNacimiento):
        self.dni = dni
        self.nombre = nombre
        self.apellidos = apellidos
        self.fechaNacimiento = fechaNacimiento
    
    def getDni(self):
        return self.dni

    def getNombre(self):
        return self.nombre

    def getApellidos(self):
        return self.apellidos

    def getFechaNacimiento(self):
        return self.fechaNacimiento
    
    def toString(self):
        print(self.dni, self.nombre, self.apellidos, self.fechaNacimiento)
