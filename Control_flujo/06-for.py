for numero in range(5):
    print(numero)

mi_lista = [1, 2, 3, 4, 5]
for elemento in mi_lista:
    print(elemento)

palabra = "palabra"

for letra in palabra:
    print(letra)

# Ejemplo de for-else
buscar = 13
for numero in range(5):
    print(numero)
    if numero == buscar:
        print("Encontrado", buscar)
        break
else:
    print("No se encontro el numero buscado. :(")
