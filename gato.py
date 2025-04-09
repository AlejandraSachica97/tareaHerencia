from animal import Animal

class Gato(Animal):
    def __init__(self, nombre, color):
        super().__init__(nombre)
        self.color = color

    def hacer_sonido(self):
        print(f"{self.nombre} dice: ¡Miau!")

    def maullar(self):
        print(f"{self.nombre} está maullando: ¡Miau Miau!")

    def mostrar_color(self):
        print(f"Color: {self.color}")
