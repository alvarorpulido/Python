correo = input("Introduce tu correo electrónico: ")
partes = correo.split("@")
if len(partes) == 2:
    nombre = partes[0]
    nuevo_correo = nombre + "@ceu.es"
    print(f"Nuevo correo: {nuevo_correo}")
else:
    print("Correo electrónico no válido.")