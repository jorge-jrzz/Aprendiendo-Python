class Perro:
    patas = 4

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    @classmethod
    def habla(cls):
        print("Guau!")

    @classmethod
    def factory(cls):
        return cls("Chanchito feliz", 4)


Perro.habla()
perro1 = Perro("Lezzi", 12)
perro2 = Perro("Chanchito", 2)
perro3 = Perro.factory()
print(perro3.edad, perro3.nombre)
