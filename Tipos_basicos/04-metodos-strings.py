animal = "  chanCHito feLiz  "

print(animal.upper())  # Cambia todos los caracteres a mayuscula.
print(animal.lower())  # Cambia todos los caracteres a minusculas.
# Pone el primer caracteres en mayuscula y todos los demas en minuscula
print(animal.capitalize())

print(animal.strip())  # Elimina los espacios del princiopio y del final.
print(animal.rstrip())  # Elimina los espacios del lado derecho.
print(animal.lstrip())  # Elimina los espacios del lado izquierdo.
print(animal.strip().capitalize())  # se pueden encadenar los metodos.

print(animal.title())  # Canbi la primeta letra de cada palabra a mayuscula.
# Regresa un indice si es que lo encuentra, y uno valor negativo si es que no lo encuentra.
print(animal.find("CH"))
# Reemplaza el primer argumento por el segundo
print(animal.replace("nCH", "j"))
print("nCH" in animal)  # Devuelve un valor booleano en la busqueda
print("nCH" not in animal)  # Devuelve un valor booleano en la busqueda
