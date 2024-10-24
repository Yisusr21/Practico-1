class Libro:
    def __init__(self, titulo, autor, genero):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero

    def mostrarInformacion(self):
        return f"Título: '{self.titulo}', Autor: '{self.autor}', Género: '{self.genero}'"


class Biblioteca:
    def __init__(self):
        self.libros = []

    def agregaLibro(self, libro):
        self.libros.append(libro)

    def buscarLibroAutor(self, autor):
        for libro in self.libros:
            if libro.autor == autor:
                return f"Tu libro encontrado por autor es: {libro.mostrarInformacion()}"
        return "No se encontraron libros del autor."

    def buscarLibroGenero(self, genero):
        for libro in self.libros:
            if libro.genero == genero:
                return f"Tu libro por el género es: {libro.mostrarInformacion()}"
        return "No se encontraron libros del género."

    def mostrarTodosLibros(self):
        if not self.libros:
            return "No hay libros en la biblioteca."
        return f"Libros en la biblioteca:\n" + "\n".join(libro.mostrarInformacion() for libro in self.libros)

    def mostrarLibro(self, titulo):
        for libro in self.libros:
            if libro.titulo == titulo:
                return f"Tu libro es: {libro.mostrarInformacion()}"
        return "No se encontró el libro."


# Libros
libro1 = Libro("Cien años de soledad", "Gabriel García Márquez", "Novela")
libro2 = Libro("1984", "George Orwell", "Distopía")
libro3 = Libro("El amor en los tiempos del cólera", "Gabriel García Márquez", "Romance")
libro4 = Libro("Fahrenheit 451", "Ray Bradbury", "Ciencia ficción")

biblioteca = Biblioteca()
biblioteca.agregaLibro(libro1)
biblioteca.agregaLibro(libro2)
biblioteca.agregaLibro(libro3)
biblioteca.agregaLibro(libro4)

# Búsquedas en la biblioteca
print("Buscamos por autor")
print(biblioteca.buscarLibroAutor("Gabriel García Márquez"))  
print("Buscamos por género")
print(biblioteca.buscarLibroGenero("Romance")) 
print(biblioteca.buscarLibroGenero("Novela"))  
print("Mostramos todos los libros")
print(biblioteca.mostrarTodosLibros())  
print("Mostramos el libro")
print(biblioteca.mostrarLibro("1984"))  

