x = float(input("Cantidad depositada en la cuenta de ahorros: "))
y = 0.04
ah1 = x * (1 + y)
ah2 = ah1 * (1 + y)
ah3 = ah2 * (1 + y)
print(f"Ahorros después del primer año: {ah1} €")
print(f"Ahorros después del segundo año: {ah2} €")
print(f"Ahorros después del tercer año: {ah3} €")