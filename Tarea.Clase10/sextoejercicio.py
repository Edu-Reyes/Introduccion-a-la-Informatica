"Bienvenido al programa sobre un catálogo de libros"

class Libro:

    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.prestado = False

    def prestar(self):
        if not self.prestado:
            self.prestado = True

    def devolver(self):
        if self.prestado:
            self.prestado = False


titulo = input("Título: ")
autor = input("Autor: ")

libro = Libro(titulo, autor)

libro.prestar()
libro.devolver()