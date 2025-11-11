palabra = input("Introduce una palabra: ")
print("Letras al revés:")
indice = len(palabra) - 1
while indice >= 0:
    print(palabra[indice])
    indice -= 1
