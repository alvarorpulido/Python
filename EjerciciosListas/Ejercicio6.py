asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
suspensas = []
for asignatura in asignaturas:
    nota = float(input(f"¿Qué nota has sacado en {asignatura}?: "))
    if nota < 5:
        suspensas.append(asignatura)
print("Asignaturas que tienes que recuperar:")
for asignatura in suspensas:
    print(asignatura)
