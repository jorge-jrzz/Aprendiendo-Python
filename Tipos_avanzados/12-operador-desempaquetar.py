lista1 = [1, 2, 3, 4, 5]

# Si nosotros quisieramos desempaquetar una lista (iterable)
print(*lista1)

lista2 = [6, 7]

conbinada = ["Hola", *lista1, "Mundo", *lista2, "Chanchito"]
print(conbinada)

# ------- DESEMPAQUETAR DICCIONARIOS ------------

punto1 = {"x": 19, "y": "hola"}
punto2 = {"y": 15}

nuevoPunto = {**punto1, "lala": "hola mundo", **punto2, "z": "mundo"}

print(nuevoPunto)
