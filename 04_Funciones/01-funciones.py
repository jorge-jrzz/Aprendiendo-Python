def hola0(nombre, apellido):    # Parapetros obligatorios
    print("Hello, World!")
    print(f"Bienvenido {nombre} {apellido}")


def hola1(nombre, apellido="Perez"):  # Parametros opcionales
    print("Hello, World!")
    print(f"Bienvenido {nombre} {apellido}")


hola0("Jorge", "Juarez")
hola1("Pedro")

# Argumentos nombrados

hola0(apellido="Vazquez", nombre="Jorge")
