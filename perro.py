from animal import Animal

class Perro(Animal):
    def __init__(self, nombre, raza):
        super().__init__(nombre)
        self.raza = raza

    def hacer_sonido(self):
        print(f"{self.nombre} dice: ¡Guau!")

    def ladrar(self):
        print(f"{self.nombre} está ladrando")

    def mostrar_raza(self):
        print(f"Raza: {self.raza}")
