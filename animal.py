class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hacer_sonido(self):
        print(f"{self.nombre} hace un sonido genérico.")

    def mostrar_nombre(self):
        print(f"Nombre: {self.nombre}")