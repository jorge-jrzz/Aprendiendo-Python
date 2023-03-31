punto = {"x": 25, "y": 50}
print(punto)
print(punto["x"])
print(punto["y"])

punto["z"] = 45
print(punto)

if "lala" in punto:
    print("encontre lala", punto["lala"])

print(punto.get("x"))
print(punto.get("lala"))
print(punto.get("lala", 12))

del punto["x"]
del (punto["y"])

print(punto)

punto["x"] = 25
for valor in punto:
    print(valor, punto[valor])


for valor in punto.items():
    print(valor)

for llave, valor in punto.items():
    print(llave, valor)

# --------------USO REAL------------------

usuarios = [
    {"id": 1, "nombre": "Chanchito"},
    {"id": 2, "nombre": "Feliz"},
    {"id": 3, "nombre": "Felipe"},
    {"id": 4, "nombre": "Jorge"}
]

for usuario in usuarios:
    print(usuario["nombre"])
