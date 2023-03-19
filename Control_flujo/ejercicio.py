"""
Bienbenido a la calculadora
Para salir escribe \"Salir\"
Las operaciones son: suma, resta, multi y div
"""
num1 = int(input("Ingresa un número: "))
op = ""
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
