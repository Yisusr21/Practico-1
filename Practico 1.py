import random



class Persona:
    def __init__(self, nombre = "", edad = 0, sexo = "Mujer", peso = 0, altura = 0):
        self._nombre = nombre
        self._edad = edad
        self._dni = self.generadorDNI()
        self._sexo = sexo
        self._peso = peso
        self._altura = altura

    def calcularIMC(self):
        if self._altura > 0 :
            masaCorporal = self._peso / (self._altura**2)
            return masaCorporal
        else:
            return 0
    
    def valorPesoCorporal(self):
        if self.calcularIMC() == 0:
            return "Altura invalidad"
        elif self.calcularIMC() < 18:
            return -1
        elif self.calcularIMC() > 25:
            return 1
        else:
            return 0
        
    def esMayorEdad(self):
        if  self._edad >= 18:
            return True
        else:
            return False
    def generadorDNI(self):
        return random.randint(10000000,99999999)
        
    #Set y get
    
    def get_nombre(self):
        return self._nombre
    
    def set_nombre(self, nombre):
        self._nombre = nombre

    def get_edad(self):
        return self._edad
    
    def set_edad(self, edad):
        self._edad = edad

    def get_peso(self):
        return self._peso
    
    def set_peso(self, peso):
        self._peso = peso

    def get_altura(self):
        return self._altura
    
    def set_altura(self, altura):
        self._altura = altura

    def get_generadorDNI(self):
        return self._dni



#return de toda la informacion

    def __str__(self):
        return f"""
        DNi: {self._dni}
        Nombre paciente: {self._nombre}
        sexo: {self._sexo}
        Edad: {self._edad}
        Es mayor: {self.esMayorEdad()}
        Peso: {self._peso}
        Altura: {self._altura}
        IMC: {self.valorPesoCorporal()}

"""
paciente = Persona()
print(paciente)

