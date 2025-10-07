precio = input("Introduce el precio del producto en euros (con dos decimales): ")
if '.' in precio:
    euros, centimos = precio.split(".")
    print(f"Euros: {euros}")
    print(f"Céntimos: {centimos}")
else:
    print("El precio debe tener dos decimales.")
