mascotas = ["Wolfgang", "Pelusa", "Chelsea", "Pulga",
            "Felipe", "Chelsea", "Chanchito feliz"]

mascotas.insert(1, "Melvin")
mascotas.append("Chanchito triste")

# Este metodo elimina el primer elemento que consida
mascotas.remove("Chelsea")

mascotas.pop()  # Elimina el ultimo elemento
mascotas.pop(1)  # Elimina el elemento del indice indicado

del mascotas[0]

mascotas.clear()

print(mascotas)
