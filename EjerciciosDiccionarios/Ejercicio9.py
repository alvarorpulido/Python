facturas = {}
cobrado = 0

while True:
    opcion = input("Añadir, pagar o salir: ")

    if opcion == 'añadir':
        num = input("Número de factura: ")
        coste = float(input("Coste: "))
        facturas[num] = coste

    elif opcion == 'pagar':
        num = input("Número de factura: ")
        if num in facturas:
            cobrado += facturas.pop(num)

    elif opcion == 'salir':
        break

    pendiente = sum(facturas.values())
    print(f"Cobrado: {cobrado}")
    print(f"Pendiente: {pendiente}")
