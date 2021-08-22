asignaturas = {
  'Matemáticas': 10,
  'Física': 10,
  'Química': 10
}

total_creditos = 0

for asignatura in asignaturas:
  print(f'{asignatura} tiene {asignaturas[asignatura]} de créditos')
  total_creditos += asignaturas[asignatura] #!valores

print(f'Total de créditos: {total_creditos}')