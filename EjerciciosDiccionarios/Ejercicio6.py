persona = {}
while True:
    clave = input("Introduce el dato que quieres añadir (o 'salir'): ")
    if clave == 'salir':
        break
    valor = input(f"Introduce el valor de {clave}: ")
    persona[clave] = valor
    print(persona)
