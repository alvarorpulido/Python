nombre = input("Introduce tu nombre: ").strip()
sexo = input("Introduce tu sexo (M para mujer, H para hombre): ").strip().upper()
if sexo == "M":
    if nombre[0].upper() < "M":
        grupo = "A"
    else:
        grupo = "B"
elif sexo == "H":
    if nombre[0].upper() > "N":
        grupo = "A"
    else:
        grupo = "B"
else:
    grupo = "Error"
print(f"Tu grupo es el {grupo}.")
