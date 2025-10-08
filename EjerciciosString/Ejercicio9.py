fechan = input("Introduce tu fecha de nacimiento (dd/mm/aaaa): ")

partes = fechan.split('/')

if len(partes) == 3:
    dia = partes[0].zfill(2)
    mes = partes[1].zfill(2)
    año = partes[2]
    
    print(f"Día: {dia}")
    print(f"Mes: {mes}")
    print(f"Año: {año}")
else:
    print("Formato incorrecto. Usa dd/mm/aaaa.")
