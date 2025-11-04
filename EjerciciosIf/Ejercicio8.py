puntuacion = float(input("Introduce tu puntuación (0.0, 0.4, 0.6 o más): "))
if puntuacion == 0.0:
    nivel = "Inaceptable"
    dinero = 2400 * 0.0
elif puntuacion == 0.4:
    nivel = "Aceptable"
    dinero = 2400 * 0.4
elif puntuacion >= 0.6:
    nivel = "Meritorio"
    dinero = 2400 * 0.6
else:
    nivel = "Puntuación no válida"
    dinero = 0
print(f"Tu nivel es: {nivel}. El dinero que recibirás es: {dinero}€.")
