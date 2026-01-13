nombre = input("Introduce tu nombre: ")
edad = input("Introduce tu edad: ")
direccion = input("Introduce tu direccion: ")
telefono = input("Introduce tu telefono: ")
datos = {'nombre':nombre,'edad':edad,'direccion':direccion,'telefono':telefono}
print(f"{datos['nombre']}, tiene {datos['edad']} años, vive en {datos['direccion']} y su telefono es {datos['telefono']}")