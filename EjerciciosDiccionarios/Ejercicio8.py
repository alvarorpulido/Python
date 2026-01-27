diccionario = {}

entrada = input("Introduce palabras y traducciones (ej. hola:hello,adiós:bye): ")
pares = entrada.split(',')

for par in pares:
    español, ingles = par.split(':')
    diccionario[español] = ingles

frase = input("Introduce una frase en español: ")
palabras = frase.split()

traduccion = []
for palabra in palabras:
    traduccion.append(diccionario.get(palabra, palabra))

print(" ".join(traduccion))
