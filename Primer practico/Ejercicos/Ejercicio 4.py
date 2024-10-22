#Ejercico 4

class Marino():
    def hablar(self):
        print("Hola...")

class Pulpo(Marino):
    def hablar(self):
        print(f"Soy un pulpo")

class Foca(Marino):
    def hablar(self , mensaje):
        self.mensaje = mensaje
        print(self.mensaje)

if __name__ == "__main__":
    marino = Marino()
    pulpo = Pulpo()
    foca = Foca ()

    pulpo.hablar()
    foca.hablar("Soy una foca")
    marino.hablar()
