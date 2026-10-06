from excepciones import LibroInvalidoError

class Libro:

    def __init__(self, titulo, autor, año):

        if titulo == "":
            raise LibroInvalidoError("El título no puede estar vacío")

        self.titulo = titulo
        self.autor = autor
        self.año = año

    def mostrar_informacion(self):
        print("Título:", self.titulo)
        print("Autor:", self.autor)
        print("Año:", self.año)