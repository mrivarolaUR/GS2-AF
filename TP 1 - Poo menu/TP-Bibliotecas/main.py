from libro import Libro
from biblioteca import Biblioteca
from excepciones import LibroInvalidoError

biblioteca = Biblioteca()

opcion = ""

while opcion != "3":

    print("\n--- Menú Biblioteca ---")
    print("1. Agregar libro")
    print("2. Mostrar libros")
    print("3. Salir")

    opcion = input("Elija una opción: ")

    if opcion == "1":

        try:
            titulo = input("Ingrese el título: ")
            autor = input("Ingrese el autor: ")
            año = input("Ingrese el año: ")

            libro = Libro(titulo, autor, año)

            biblioteca.agregar_libro(libro)

            print("Libro agregado")

        except LibroInvalidoError as error:
            print("Error:", error)

    elif opcion == "2":

        biblioteca.mostrar_libros()

    elif opcion == "3":

        print("Programa finalizado")

    else:

        print("Opción incorrecta")