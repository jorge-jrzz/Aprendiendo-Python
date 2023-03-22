numeros = [2, 4, 23, 67, 1, 8, 22]
# print(numeros)

# numeros.sort()
# print(numeros)

# numeros.sort(reverse=True)
# print(numeros)

# Este metodo crea otra lista sin afectar la original
# numeros2 = sorted(numeros)
# print(numeros2)
# numeros2 = sorted(numeros, reverse=True)
# print(numeros)
# print(numeros2)

# usuarios = [[4, "Chanchito"], [1, "Felipe"], [5, "Pulga"]]
# print(usuarios)
# usuarios.sort()
# print(usuarios)

usuarios = [["Chanchito", 4], ["Felipe", 1], ["Pulga", 5]]
print(usuarios)


def ordena(elemento):
    return elemento[1]


usuarios.sort(key=ordena)
print(usuarios)

usuarios.sort(key=ordena, reverse=True)
print(usuarios)
