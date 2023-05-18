class Perro:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f"Clase Perro: {self.nombre}"

    def habla(self):
        print(f"{self.__nombre} dice Guau!")


perro = Perro("chanchito", 4)
print(perro)
texto = str(perro)
print(texto)
