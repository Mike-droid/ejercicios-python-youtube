def run():
  def crear_diccionario(frase):
    frase = frase.split(' ')
    print(frase)
    diccionario = {}
    for palabra in frase:
      longitud = len(palabra)
      diccionario[palabra] = longitud
    return diccionario

  mi_frase = 'Soy una frase y está es otra palabra'
  print(crear_diccionario(mi_frase))


if __name__ == '__main__':
  run()