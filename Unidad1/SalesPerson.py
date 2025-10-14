# En la siguiente clase SalesPerson, agrega dos variables de clase llamadas total_revenue y names. La variable names debe ser una 
# lista que contenga los nombres de todos los alumnos de clase y total_revenue debe contener el monto total de ventas de todos los vendedores.
import random


class SalesPerson:
    total_revenue = 0
    names = []

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.sales_amount = 0
        SalesPerson.names.append(name)

    def make_sale(self, money):
        self.sales_amount += money
        SalesPerson.total_revenue += money

    def show(self):
        print(self.name, self.age, self.sales_amount)


alumnos = []

for i in range(1, 12):
    edad = random.randint(18, 65)
    alumno = SalesPerson(f"Alumno {i}", edad)
    alumnos.append(alumno)

print("\n--- REGISTRO DE VENTAS ---")
for alumno in alumnos:
    venta = random.randint(1000, 5000)
    alumno.make_sale(venta)

print("\n--- INFORME DE VENDEDORES ---")
for alumno in alumnos:
    alumno.show()

print("\nNombres de vendedores:", SalesPerson.names)
print("Total de ventas:", SalesPerson.total_revenue)


# Por si queremos acceder a el dato de un alumno concreto
alumno1 = alumnos[9]
print(alumno1.name)

for alumno in alumnos:
    if alumno.name == "Alumno 3":
        print(alumno.name)