numero = int(input("Introduce un número entero: "))
if numero > 1:
    es_primo = True
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            es_primo = False
            break
    if es_primo:
        print("Es un número primo.")
    else:
        print("No es un número primo.")
else:
    print("No es un número primo.")