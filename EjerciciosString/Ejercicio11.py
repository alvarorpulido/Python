nombre = input("Nombre del producto: ")
precio = float(input("Precio unitario: "))
unidades = int(input("Número de unidades: "))
total = precio * unidades
print(f"{nombre}: {precio:09.2f} €, unidades: {unidades:03d}, coste total: {total:011.2f} €")