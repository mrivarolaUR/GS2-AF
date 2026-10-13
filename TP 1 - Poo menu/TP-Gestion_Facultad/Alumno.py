class Alumno:  # Creamos la clase Alumno

    def __init__(self, dni, nombre, apellido, carrera):  # Constructor de la clase
        self.dni = dni  # Guardamos el DNI del alumno
        self.nombre = nombre  # Guardamos el nombre
        self.apellido = apellido  # Guardamos el apellido
        self.carrera = carrera  # Guardamos la carrera actual
        self.materias_aprobadas = []  # Creamos una lista vacía para las materias aprobadas


    # GETTERS
    # Los getters sirven para obtener o consultar los datos

    def get_dni(self):  # Getter del DNI
        return self.dni  # Devolvemos el DNI

    def get_nombre(self):  # Getter del nombre
        return self.nombre  # Devolvemos el nombre

    def get_apellido(self):  # Getter del apellido
        return self.apellido  # Devolvemos el apellido

    def get_carrera(self):  # Getter de la carrera
        return self.carrera  # Devolvemos la carrera

    def get_materias(self):  # Getter de las materias
        return self.materias_aprobadas  # Devolvemos la lista de materias


    # SETTERS
    # Los setters sirven para modificar los datos

    def set_dni(self, dni):  # Setter del DNI
        self.dni = dni  # Cambiamos el DNI

    def set_nombre(self, nombre):  # Setter del nombre
        self.nombre = nombre  # Cambiamos el nombre

    def set_apellido(self, apellido):  # Setter del apellido
        self.apellido = apellido  # Cambiamos el apellido

    def set_carrera(self, carrera):  # Setter de la carrera

        # Verificamos que la carrera exista
        if carrera == "IT" or carrera == "DS" or carrera == "AF":
            self.carrera = carrera  # Cambiamos la carrera

        else:
            raise Exception("La carrera no existe")  # Mostramos un error

    # MATERIAS

    def agregar_materia(self, materia):  # Método para agregar una materia aprobada
        self.materias_aprobadas.append(materia)  # Agregamos la materia a la lista

    # MOSTRAR INFORMACIÓN

    def mostrar_info(self):  # Método para mostrar los datos del alumno

        print("DNI:", self.dni)  # Mostramos el DNI
        print("Nombre:", self.nombre)  # Mostramos el nombre
        print("Apellido:", self.apellido)  # Mostramos el apellido
        print("Carrera:", self.carrera)  # Mostramos la carrera

    def mostrar_materias(self):  # Método para mostrar las materias aprobadas

        print("Materias aprobadas:")  # Mostramos un título

        for materia in self.materias_aprobadas:  # Recorremos la lista de materias
            print("-", materia)  # Mostramos cada materia