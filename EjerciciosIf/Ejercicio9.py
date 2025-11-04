edad = int(input("Introduce tu edad: "))
if edad < 4:
    precio = 0
elif 4 <= edad <= 18:
    precio = 5
else:
    precio = 10
print(f"El precio de entrada es: {precio}€.")
