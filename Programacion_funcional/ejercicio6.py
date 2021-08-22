def run():
  def califica(nota):
    if nota < 6:
      return 'Reprobado/a'
    elif nota >= 6 and nota < 8:
      return 'Regular'
    elif nota >= 8 and nota < 9:
      return 'Bien'
    elif nota >= 9:
      return 'Excelente'


  notas = [4,5,5,6]

  def crea_lista_calificaciones(lista_nota):
    return list(map(califica, notas))


  print(crea_lista_calificaciones(notas))


if __name__ == '__main__':
  run()
