def run():
  def aplicar_descuento(precio, descuento):
    return precio - ((precio * descuento)/100) #20 -> 0.20


  def aplicar_iva(precio, iva):
    return precio + ((precio * iva)/100)


  def precio_cesta(funcion, cesta):
    total = 0
    for precio, porcentaje in cesta.items():
      total += funcion(precio, porcentaje)
    return total


  cesta1 = {
    700: 22,
    4000: 12,
    500: 10
  }

  cesta2 = {
    320: 8,
    900: 11,
    670: 9
  }

  print(f'El precio de la cesta1 después de aplicar los descuentos es {precio_cesta(aplicar_descuento, cesta1)}')
  print(f'El precio de la cesta2 después de aplicar el IVA es: {precio_cesta(aplicar_iva, cesta2)}')


if __name__ == '__main__':
  run()