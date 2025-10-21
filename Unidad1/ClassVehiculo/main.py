from Bicicleta import Bicicleta
from Coche import Coche
from Vehiculo import Vehiculo

def menu():
    # Crear los objetos con kilómetros iniciales = 0
    bici = Bicicleta(0)
    coche = Coche(0)

    while True:
        print("""
            1. Anda con la bicicleta
            2. Haz el caballito con la bicicleta
            3. Anda con el coche
            4. Quema rueda con el coche
            5. Ver kilometraje de la bicicleta
            6. Ver kilometraje del coche
            7. Ver kilometraje total
            8. Salir
        """)

        opcion = input("Elige una opción (1-8): ")

        match opcion:
            case "1":
                km = int(input("¿Cuántos kilómetros quiere recorrer? "))
                bici.anda(km)
            case "2":
                bici.hacer_caballito()
            case "3":
                km = int(input("¿Cuántos kilómetros quiere recorrer? "))
                coche.anda(km)
            case "4":
                coche.quemar_rueda()
            case "5":
                print(f"La bicicleta lleva recorridos {bici.kilometrosRecorridos} km")
            case "6":
                print(f"El coche lleva recorridos {coche.kilometrosRecorridos} km")
            case "7":
                print(f"Los vehículos llevan recorridos {Vehiculo.kilometrosTotales} km")
            case "8":
                print("¡Hasta la próxima!")
                break
            case _:
                print("Opción no válida.")

if __name__ == "__main__":
    menu()
