def contar_palabras(frase):
    palabras = frase.split()
    dicc = {}
    repetidas = []
    for palabra in palabras:
        if palabra in dicc:
            dicc[palabra] += 1
        else:
            dicc[palabra] = 1
    for palabra in dicc:
        if dicc[palabra] > 1:
            repetidas.append(palabra)
    return dicc, repetidas
frase = input("Introduce la frase para contar palabras: ")
diccionario, lista_rep = contar_palabras(frase)
print(diccionario)
print(lista_rep)

