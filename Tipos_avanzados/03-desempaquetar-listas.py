numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# feo!
# primero = numeros[0]
# segundo = numeros[1]
# tercero = numeros[2]

# primero, segundo, tercero = numeros
# print(primero, segundo, tercero)

# primero, *otros = numeros
# print(primero, otros)

# primero, segundo, *otros = numeros
# print(primero, segundo, otros)

# primero, *otros, ultimo = numeros
# print(primero, ultimo, otros)

primero, segundo, *otros, penultimo, ultimo = numeros
print(segundo, penultimo, otros)
