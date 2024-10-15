#Ejercicio 2
class Calculadora:
    def __init__(self,):
        self.num1 = int(input("Intorudoce un numero: "))
        self.num2 = int(input("Introduce otro numero: "))

    def suma(self):
        print(self.num1 + self.num2)

    def resta(self):
        return self.num1 - self.num2
    
    def multiiplicacion(self):
        return self.num1 * self.num2
    
    def division (self):
        return self.num1 // self.num2

calculadora = Calculadora()
print(F"La suma es: {calculadora.suma()} \nla resta es: {calculadora.resta()} \nla multiplcacion es: {calculadora.multiiplicacion()} \nla divison entera es: {calculadora.division()}")