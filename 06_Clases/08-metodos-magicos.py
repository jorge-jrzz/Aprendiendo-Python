class Perro:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __del__(self):
        print(f"Chau Perro {self.nombre}")

    def __str__(self):
        return f"Clase Perro: {self.nombre}"

    def habla(self):
        print(f"{self.__nombre} dice Guau!")


perro = Perro("chanchito", 4)
print(perro)
del perro
# print(perro)    # Error
