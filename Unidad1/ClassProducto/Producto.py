class Producto():
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def aplicar_descuento(self, porcentaje):
        if porcentaje >= 0 and porcentaje <= 100:
            self.precio = round(self.precio - (self.precio * porcentaje / 100), 2)
            print(self.precio)
        else:
            print("El descuento tiene que estar entyre 0 y 100")
    
    @classmethod
    def desde_texto(cls, texto):
        nombre, precio = texto.split(",")
        cls(nombre, precio)

    @staticmethod
    def es_precio_valido(precio):
        return precio > 0
    


producto = Producto("camiseta", 19.99)
producto.aplicar_descuento(20)
print(producto.es_precio_valido(producto.precio))