numero = 1
# while numero < 100:
#     print(numero)
#     numero *= 2


# El siguinete code simula una terminar
comando = ""
while comando.lower() != "salir":
    # Se ocupa el comando de lower para que el usuario pueda ingresar: $ SALIR, $ Salir o $ SaLiR
    comando = input("$ ")
    print(comando)

''' 
while True:
    comando = input("$ ")
    print(comando)
    if comando.lower() == "salir":
        break;
'''
