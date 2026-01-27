clientes = {}

while True:
    opcion = input("1-Añadir 2-Eliminar 3-Mostrar 4-Listar 5-Preferentes 6-Salir: ")

    if opcion == '1':
        nif = input("NIF: ")
        clientes[nif] = {
            'nombre': input("Nombre: "),
            'dirección': input("Dirección: "),
            'teléfono': input("Teléfono: "),
            'correo': input("Correo: "),
            'preferente': input("Preferente (True/False): ") == 'True'
        }

    elif opcion == '2':
        nif = input("NIF: ")
        clientes.pop(nif, None)

    elif opcion == '3':
        nif = input("NIF: ")
        print(clientes.get(nif, "Cliente no encontrado"))

    elif opcion == '4':
        for nif, datos in clientes.items():
            print(nif, datos['nombre'])

    elif opcion == '5':
        for nif, datos in clientes.items():
            if datos['preferente']:
                print(nif, datos['nombre'])

    elif opcion == '6':
        break
