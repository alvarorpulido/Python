lista = [50, 4, 28, 33, 12]
suma = 0
aciertos = 0
print("SUMAR Y GANAR")
print("Sume todos los número empezando por 0.")
for numero in lista:
    respuesta = int(input(f"Más {numero}: "))
    suma_correcta = suma + numero
    if respuesta == suma_correcta:
        suma = respuesta
        aciertos += 1
    else:
        print(f"Te has equivocado, pero has acertado {aciertos} veces seguidas.")
        break
else:
    print("Enhorabuena, GANASTE.")