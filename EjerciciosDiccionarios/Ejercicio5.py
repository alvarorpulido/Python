asignaturas = {'Matemáticas': 6, 'Física': 4, 'Química': 5}
total = 0

for asignatura, creditos in asignaturas.items():
    print(f"{asignatura} tiene {creditos} créditos")
    total += creditos

print(f"Total de créditos: {total}")
