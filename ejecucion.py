from perro import Perro
from gato import Gato

if __name__ == "__main__":
    tipo_animal = input("¿Qué tipo de animal quieres crear (perro/gato)? ").lower()

    if tipo_animal == "perro":
        nombre_perro = input("Ingresa el nombre del perro: ")
        raza_perro = input("Ingresa la raza del perro: ")
        mi_perro = Perro(nombre_perro, raza_perro)
        mi_perro.mostrar_nombre()
        mi_perro.mostrar_raza()
        mi_perro.hacer_sonido()
        mi_perro.ladrar()
    elif tipo_animal == "gato":
        nombre_gato = input("Ingresa el nombre del gato: ")
        color_gato = input("Ingresa el color del gato: ")
        mi_gato = Gato(nombre_gato, color_gato)
        mi_gato.mostrar_nombre()
        mi_gato.mostrar_color()
        mi_gato.hacer_sonido()
        mi_gato.maullar()
    else:
        print("Tipo de animal no reconocido.")