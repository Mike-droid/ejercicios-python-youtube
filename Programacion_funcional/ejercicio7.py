def run():
  def crea_diccionario(diccionario):
    nuevo_diccionario = {}
    for asignatura, nota in diccionario.items():
      asignatura = asignatura.upper()
      if nota < 6:
        nota = 'Reprobado'
      elif nota < 8:
        nota = 'Regular'
      elif nota < 10:
        nota = 'Excelente'
      elif nota == 10:
        nota = 'Perfecto'

      nuevo_diccionario[asignatura] = nota

    return nuevo_diccionario

  asignaturas_notas = {
    'Español': 5,
    'Matemáticas': 7,
    'Inglés': 9,
    'Bases de datos': 10
  }

  print(crea_diccionario(asignaturas_notas))


if __name__ == '__main__':
  run()
