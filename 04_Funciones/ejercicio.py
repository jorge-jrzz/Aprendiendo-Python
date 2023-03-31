# 2 funciones, una que elimine los espacion en blando de una cadena, y otra funcion que realice el reverse a la cadena

def elimina_espacios(texto):
    text = ""
    for palabra in texto:
        if palabra != " ":
            text += palabra
    return text


def vuelta(texto):
    letras = len(texto)
    text = ""
    for _ in texto:
        text += texto[letras-1]
        letras -= 1
    return text


def es_palindromo(texto):
    text = elimina_espacios(texto)
    text = vuelta(text)

    texto = elimina_espacios(texto)

    if texto.lower() == text.lower():
        return "Es Palindromo :)"
    else:
        return "No es Palindromo :("


print("Pedro, ", es_palindromo("Pedro"))


'''
# Implementacion del Profe:

def no_space(texto):
    nuevo_texto = ""
    for char in texto:
        if char != " ":
            nuevo_texto += char
    return nuevo_texto


def reverse(texto):
    texto_al_reves = ""
    for char in texto:
        # Concatena los chars en de izquierda a derecha
        texto_al_reves = char + texto_al_reves
    return texto_al_reves


def es_palindromo(texto):
    texto = no_space(texto)
    texto_al_reves = reverse(texto)
    return texto.lower() == texto_al_reves.lower()


print("Amo la paloma")
print("Hola Mundo")
'''
