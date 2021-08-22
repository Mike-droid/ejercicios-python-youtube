def calcula_total_factura(precio, iva = 21):
  iva /= 100
  total = (precio * iva) + precio
  print(f"El precio total es de ${total}")

calcula_total_factura(1000 , 5)
calcula_total_factura(1000)