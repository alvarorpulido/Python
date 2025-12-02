numeros = []
print("Introduce los 6 números ganadores de la lotería primitiva:")
for i in range(6):
    numero = int(input(f"Número {i+1}: "))
    numeros.append(numero)
numeros_ordenados = sorted(numeros)
print("\nNúmeros ganadores ordenados de menor a mayor:")
print(numeros_ordenados)
