def run():
  def crea_diccionario(diccionario):
    nuevo_diccionario = {}
    for asignatura, nota in diccionario.items():
      asignatura = asignatura.upper()
      if nota >= 7:
        nota = 'Aprobado'
        nuevo_diccionario[asignatura] = nota

    return nuevo_diccionario

  asignaturas_notas = {
    'Español': 5,
    'Matemáticas': 7,
    'Inglés': 9,
    'Arte': 4
  }

  print(crea_diccionario(asignaturas_notas))


if __name__ == '__main__':
  run()
