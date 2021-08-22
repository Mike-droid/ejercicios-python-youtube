asignaturas_lista = ['Matemáticas', 'Física', 'Química', 'Historia', 'Lengua'] # len = 5
calificaciones_lista = []

for asignatura in asignaturas_lista:
  calificacion = float(input(f'¿Qué calificación obtuviste en {asignatura}?: '))
  calificaciones_lista.append(calificacion)

for i in range(len(asignaturas_lista)):
  print(f'En {asignaturas_lista[i]} conseguiste {calificaciones_lista[i]}')