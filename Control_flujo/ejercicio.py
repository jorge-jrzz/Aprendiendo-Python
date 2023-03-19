bienvenida = """
Bienbenido a la calculadora
Para salir escribe \"Salir\"
Las operaciones son: suma, resta, multi y div
"""
print(bienvenida)
num1 = int(input("Ingresa un número: "))
while True:
    op = input("Ingresa operacion: ")
    if op.lower() == "salir":
        break
    num2 = int(input("Ingresa siguinet número: "))
    if op.lower() == "suma":
        num1 = num1 + num2

    elif op.lower() == "resta":
        num1 = num1 - num2

    elif op.lower() == "multi":
        num1 = num1 * num2

    elif op.lower() == "div":
        num1 = num1 / num2
    else:
        print("ERROR")

    print("El resultado es: ", num1)


# Implementacion del Profe:

print("Bienvenidos a la calculadora")
print("Para salir escribe salir")
print("Las operaciones son: suma, resta, multi y div")

resultado = ""
while True:
    if not resultado:
        resultado = input(" Ingrese número ")
        if resultado.lower() == "salir":
            break
        resultado = int(resultado)
    op = input("Ingresa operación: ")
    if op.lower() == "salir":
        break
    n2 = input("ingresa siguinte número: ")
    if op.lower() == "salir":
        break
    n2 = int(n2)

    if op.lower() == "suma":
        resultado += n2
    elif op.lower() == "resta":
        resultado -= n2
    elif op.lower() == "multi":
        resultado *= n2
    elif op.lower() == "div":
        resultado /= n2
    else:
        print("Operacion no valida")
        break

    print(f"El resultado es: {resultado}")
