asignaturas_lista = ['Matemáticas', 'Física', 'Química', 'Historia', 'Lengua']
asignaturas_a_repetir = []

for asignatura in asignaturas_lista:
  nota = float(input(f'¿Qué calificación obtuviste en {asignatura}?: '))
  if nota < 7:
    asignaturas_a_repetir.append(asignatura)

print(f'Debes repetir {asignaturas_a_repetir}')