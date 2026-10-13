from Alumno import Alumno  # Importamos la clase Alumno
from Facu import Facultad  # Importamos la clase Facultad


facultad = Facultad()  # Creamos la facultad


while True:  # Repetimos el menú hasta elegir salir

    print("\n--- SISTEMA DE FACULTAD ---")
    print("1 - Agregar alumno")
    print("2 - Ver alumnos")
    print("3 - Agregar materia aprobada")
    print("4 - Ver alumnos y materias")
    print("5 - Cambiar carrera")
    print("6 - Salir")

    opcion = input("Elegí una opción: ")  # Pedimos una opción


    if opcion == "1":

        dni = input("DNI: ")  # Pedimos el DNI
        nombre = input("Nombre: ")  # Pedimos el nombre
        apellido = input("Apellido: ")  # Pedimos el apellido
        carrera = input("Carrera (IT / DS / AF): ")  # Pedimos la carrera

        alumno = Alumno(dni, nombre, apellido, carrera)  # Creamos el alumno

        facultad.agregar_alumno(alumno)  # Agregamos el alumno a la facultad

        print("Alumno agregado correctamente")


    elif opcion == "2":

        facultad.mostrar_alumnos()  # Mostramos todos los alumnos


    elif opcion == "3":

        dni = input("Ingrese el DNI del alumno: ")  # Pedimos el DNI

        for alumno in facultad.alumnos:  # Recorremos los alumnos

            if alumno.get_dni() == dni:  # Buscamos el alumno por DNI

                materia = input("Ingrese la materia aprobada: ")  # Pedimos la materia

                alumno.agregar_materia(materia)  # Agregamos la materia

                print("Materia agregada correctamente")

                break  # Terminamos la búsqueda

        else:
            print("Alumno no encontrado")


    elif opcion == "4":

        facultad.mostrar_alumnos_y_materias()  # Mostramos alumnos y materias


    elif opcion == "5":

        dni = input("Ingrese el DNI del alumno: ")  # Pedimos el DNI

        for alumno in facultad.alumnos:  # Recorremos los alumnos

            if alumno.get_dni() == dni:  # Buscamos el alumno

                nueva_carrera = input("Nueva carrera (IT / DS / AF): ")  # Pedimos la nueva carrera

                try:
                    alumno.set_carrera(nueva_carrera)  # Cambiamos la carrera

                    print("Carrera cambiada correctamente")

                except Exception as error:
                    print(error)  # Mostramos el error

                break  # Terminamos la búsqueda

        else:
            print("Alumno no encontrado")


    elif opcion == "6":

        print("Programa finalizado")
        break  # Salimos del while


    else:

        print("Opción incorrecta")  # Avisamos que la opción no existe