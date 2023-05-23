try:
    n1 = int(input("Ingresa primer numero: "))
    linea_de_codigo_sin_sentido

except ValueError as e:
    print("Ingrese un valor que corresponda")

except NameError as e:
    print("Ocurrio un error")
