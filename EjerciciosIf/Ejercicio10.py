tipo_pizza = input("¿Quieres una pizza vegetariana? (si/no): ").strip().lower()
if tipo_pizza == "si":
    ingredientes = ["Pimiento", "Tofu"]
    tipo = "vegetariana"
elif tipo_pizza == "no":
    ingredientes = ["Peperoni", "Jamón", "Salmón"]
    tipo = "no vegetariana"
else:
    print("Opción no válida.")
    exit()
print("Ingredientes disponibles:")
for i, ingrediente in enumerate(ingredientes, 1):
    print(f"{i}. {ingrediente}")
opcion = int(input("Elige un ingrediente (1 o 2): "))
ingrediente_elegido = ingredientes[opcion - 1]
print(f"Has elegido una pizza {tipo} con los ingredientes: Mozzarella, Tomate y {ingrediente_elegido}.")
