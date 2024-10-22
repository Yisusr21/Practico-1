#Ejercico 3

class Fabrica:
    def __init__(self, llantas, color, precio):
        self.llantas = llantas
        self.color = color
        self.precio = precio

class Moto(Fabrica):    
    def __init__(self, llantas, color, precio,):
        super().__init__(llantas, color, precio)
    
    def __str__(self):
        return f"Moto: tiene {self.llantas} llantas, es de color {self.color} y tiene un precio de {self.precio}"

class Auto(Fabrica):
    def __init__(self, llantas, color, precio):
        super().__init__(llantas, color, precio)
    def __str__(self):
        return f"Auto: tiene {self.llantas} llantas, es de color {self.color} y tiene un precio de {self.precio}"

auto = Auto(4,"Rojo", 10000)
moto = Moto(2, "Azul", 5000)
print(auto)
print(moto)