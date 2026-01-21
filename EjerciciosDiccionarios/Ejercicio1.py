divisas = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}
moneda = input("Introduce una divisa: ")

if moneda in divisas:
    print(f"El símbolo es: {divisas[moneda]}")
else:
    print("La divisa no está en el diccionario.")