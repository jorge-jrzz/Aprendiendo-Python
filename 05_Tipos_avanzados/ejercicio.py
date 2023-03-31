# 1. Eliminar los espacios en blanco de un string
# y devolver una lista con los caracteres restantes

# 2. Contar en un diccionario cuanto se repiten
# los caracteres de un string

# 3. Ordenar las llaves de un diccionario
# por el valor que tienen y devolver una lista
# que contiene tuplas [("a",3),("b",2),("c",4),("d", 4)]

# 4. De un listado de tuplas,devolver las tuplas
# que tengan el mayor valor.
# [("a",3),("b",2),("c",4)] ->【("c",4)】

# 5. Crear un mensaje que diga:
# Los caracteres que mas se repiten con 4 repeticiones son:
# - C
# - D

# 6. Juntar la solucion de los ejercicios anteriores
# para encontrar los caracteres que mas se repiten
# de un string


# -------Implementacion del Profe-------

string = "Hola mundo este es mi string"


def quita_espacios(texto):
    return [char for char in texto if char != " "]


def cuanta_caracteres(lista):
    chars_dict = {}
    for char in lista:
        if char in chars_dict:
            chars_dict[char] += 1
        else:
            chars_dict[char] = 1
    return chars_dict


def ordena(dict):
    return sorted(
        dict.items(),
        key=lambda key: key[1],
        reverse=True
    )


def mayore_tuplas(lista):
    maximo = lista[0][1]
    respuesta = {}
    for orden in lista:
        if maximo > orden[1]:
            break
        respuesta[orden[0]] = orden[1]
    return respuesta


def crea_mensaje(diccionario):
    mensaje = "Los caracteres que mas se repiten son: \n"
    for key, valor in diccionario.items():
        mensaje += f"- {key}, con {valor} repticiones \n"
    return mensaje


sin_espacios = quita_espacios(string)
# print(sin_espacios)

contados = cuanta_caracteres(sin_espacios)
# pprint(contados, width=1)

ordenados = ordena(contados)
print(ordenados)

mayores = mayore_tuplas(ordenados)
print(mayores)

mensaje = crea_mensaje(mayores)
print(mensaje)
