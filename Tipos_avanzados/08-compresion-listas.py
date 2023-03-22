usuarios = [
    ["Chanchito", 4],
    ["Felipe", 1],
    ["Pulga", 5]
]

# nombres = []
# for usuario in usuarios:
#     nombres.append(usuario[0])
# print(nombres)

# nombres = [usuario[0] for usuario in usuarios]

# nombres = [usuario for usuario in usuarios if usuario[1] > 2] # Filtar listas

nombres = [usuario[0]
           for usuario in usuarios if usuario[1] > 2]  # Filtar listas

print(nombres)
