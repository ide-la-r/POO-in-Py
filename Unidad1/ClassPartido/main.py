from Jugadores import Jugadores
from Equipo import Equipo
from Partido import Partido

def main():
    # Crear equipos
    nombre_eq1 = input("Nombre del equipo 1: ")
    nombre_eq2 = input("Nombre del equipo 2: ")
    equipo1 = Equipo(nombre_eq1)
    equipo2 = Equipo(nombre_eq2)

    # Crear partido
    partido = Partido(equipo1, equipo2)

    while True:
        print(f"""
            --- MENÚ ---
            1. Añadir jugador al {equipo1.nombre}
            2. Añadir jugador al {equipo2.nombre}
            3. Anotar goles al {equipo1.nombre}
            4. Anotar goles al {equipo2.nombre}
            5. Ver marcador
            6. Finalizar partido
            7. Salir
        """)
        opcion = input("Elige una opción (1-7): ")

        match opcion:
            case "1":
                nombre = input("Nombre del jugador: ")
                numero = input("Número del jugador: ")
                posicion = input("Posición del jugador: ")
                jugador = Jugadores(nombre, numero, posicion)
                equipo1.aniadir_jugadores(jugador)

            case "2":
                nombre = input("Nombre del jugador: ")
                numero = input("Número del jugador: ")
                posicion = input("Posición del jugador: ")
                jugador = Jugadores(nombre, numero, posicion)
                equipo2.aniadir_jugadores(jugador)

            case "3":
                goles = int(input(f"¿Cuántos goles anota {equipo1.nombre}? "))
                partido.anotar_goles(goles, equipo1)

            case "4":
                goles = int(input(f"¿Cuántos goles anota {equipo2.nombre}? "))
                partido.anotar_goles(goles, equipo2)

            case "5":
                print(f"Marcador actual: {equipo1.nombre} {equipo1.goles} - {equipo2.goles} {equipo2.nombre}")

            case "6":
                partido.finalizar_partido()
                break

            case "7":
                print("Saliendo del programa...")
                break

            case _:
                print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    main()
