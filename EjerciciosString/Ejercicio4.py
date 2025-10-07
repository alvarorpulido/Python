telefono = input("Introduce el número de teléfono (formato +34-XXXXXXXXX-XX): ")
partes = telefono.split("-")
if len(partes) == 3 and partes[0] == "+34":
    print(f"Número sin prefijo ni extensión: {partes[1]}")
else:
    print("Formato incorrecto.")