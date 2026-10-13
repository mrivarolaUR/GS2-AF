class Facultad:  # Creamos la clase Facultad

    def __init__(self):  # Constructor de la clase
        self.carreras = ["IT", "DS", "AF"]  # Guardamos las carreras disponibles
        self.alumnos = []  # Creamos una lista vacía de alumnos


    def agregar_alumno(self, alumno):  # Método para agregar un alumno
        self.alumnos.append(alumno)  # Agregamos el alumno a la lista


    def mostrar_alumnos(self):  # Método para mostrar todos los alumnos

        for alumno in self.alumnos:  # Recorremos la lista de alumnos
            alumno.mostrar_info()  # Mostramos la información del alumno
            print()  # Dejamos un espacio


    def mostrar_alumnos_y_materias(self):  # Método para mostrar alumnos y sus materias

        for alumno in self.alumnos:  # Recorremos todos los alumnos

            alumno.mostrar_info()  # Mostramos los datos del alumno

            alumno.mostrar_materias()  # Mostramos sus materias aprobadas

            print()  # Dejamos un espacio entre alumnos