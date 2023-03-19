
saludo = 25


def saludar():
    global saludo
    saludo = "Hola Mundo"


def saludaChanchito():
    saludo = 24
    print(saludo)


resultado1 = saludo + 3
print(resultado1)
saludar()
# En la siguinete parte el codigo se rompe, por que el valor de saludo ahora es un string
# y no un numero entero (esto por que se modifico en la funcio "saludar").
# Por esta razon no se recomienda usar variable globales
resultado2 = saludo + 4
print(saludo)
