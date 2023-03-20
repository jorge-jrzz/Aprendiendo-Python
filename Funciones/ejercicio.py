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
