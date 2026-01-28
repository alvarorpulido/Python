saldo = 0
Ingresos = []
Reintegros = []
while True:
    preg = int(input("¿Que desea realizar? (1. Ingreso, 2. Reintegro): "))
    if preg == 1:
        ing = int(input("¿Cuánto desea ingresar?: "))
        saldo += ing
        Ingresos.append(ing)
        print (f"Saldo actual: {saldo}")
    if preg == 2:
        rein = int(input("¿Cuánto desea reintegrar?: "))
        if rein > saldo:
            print ("No hay saldo suficiente")
        else:
            saldo -= rein
            neg = int(-(rein))
            Reintegros.append(neg)
            print (f"Saldo actual: {saldo}")
    elif preg != 1 and preg != 2:
        print("Saliendo del menú")
        break
print(f"Ingresos: {Ingresos}")
print(f"Reintegros: {Reintegros}")


