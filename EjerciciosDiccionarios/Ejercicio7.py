cesta = {}

while True:
    articulo = input("Artículo (o 'fin'): ")
    if articulo == 'fin':
        break
    precio = float(input("Precio: "))
    cesta[articulo] = precio

print("\nLista de la compra")
total = 0
for articulo, precio in cesta.items():
    print(f"{articulo} {precio}")
    total += precio

print(f"Total {total}")
