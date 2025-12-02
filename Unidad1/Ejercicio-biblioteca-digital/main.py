from LibroDigital import LibroDigital
from VideoCurso import VideoCurso
from Podcast import Podcast
from BibliotecaDigital import BibliotecaDigital

def main():
    libro1 = LibroDigital("Cien años de soledad", "Gabriel García Márquez", 1967, 417, "PDF")
    videocurso1 = VideoCurso("Curso de Python avanzado", "Ana Programadora", 2023, 180, "Intermedio")
    podcast1 = Podcast("Historia en 10 minutos", "Historiador Pro", 2024, 50, "Historia Mundial")

    biblioteca = BibliotecaDigital()

    biblioteca.aniadir_recurso(libro1)
    biblioteca.aniadir_recurso(videocurso1)
    biblioteca.aniadir_recurso(podcast1)

    print("--- Listando Recursos ---")
    biblioteca.listar_recursos()

    print("--- Abriendo todos los Recursos ---")
    biblioteca.abrir_todos()

    print("--- Modificando atributos ---")
    podcast1.set_titulo("La Historia de Roma: Edición Especial")
    print(f"Título modificado del Podcast: {podcast1.get_titulo()}")
    
    libro1.set_anio(2025)
    print(f"Año modificado del Libro: {libro1.get_anio()}")
    
if __name__ == "__main__":
    main()