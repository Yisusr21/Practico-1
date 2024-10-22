
class Universidad:
    def __init__(self, nameuniversidad):
        self.nameuniversidad = nameuniversidad


class Carrera:
    def __init__(self, especialidad):
        self.especialidad = especialidad


class Estudiante(Universidad, Carrera):
    def __init__(self, nombre, apellido, edad, nameuniversidad, especialidad):
        super().__init__(nameuniversidad)
        super().__init__(especialidad)
        self.nameuniversidad = nameuniversidad
        self.especialidad = especialidad
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        
    def __str__(self):
        return f"El estudiante de nombre y apellido {self.nombre} {self.apellido} de edad {self.edad} años, se encuentra en la universidad {self.nameuniversidad} cursando {self.especialidad}"
    

persona =Estudiante("Jesus", "Jimenez", 23, "UNICEN", "Ingeneria de Sistema")

print(persona)