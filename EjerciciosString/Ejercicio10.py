productos = input("Introduce los productos separados por comas: ")
listaprod = [producto.strip() for producto in productos.split(',')]
print("Productos:")
for producto in listaprod:
    print(producto)