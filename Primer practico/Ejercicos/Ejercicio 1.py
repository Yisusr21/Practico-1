#Ejercicio 1

class Estudiante:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota
    def resultadoFinal(self):
        if self.nota >= 4:
            return f"El estudiante {self.nombre} ha aprobo"
        else:
            return f"El estudiante {self.nombre} usted a desaprobado"

estudiante=Estudiante("Jesus Jimenez", 6)
print(estudiante.resultadoFinal())
