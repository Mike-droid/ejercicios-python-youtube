facturas_pendientes = {}

menu = """
1. Añadir nueva factura
2. Pagar factura
3. Terminar
"""

while True:
  print(menu)
  opcion = int(input("¿Qué deseas hacer?: "))

  if opcion == 1:
    clave_factura = input("Escribe la clave de la factura: ")
    valor_factura = float(input("Escribe el precio de la factura: "))
    nuevo = facturas_pendientes.setdefault(clave_factura , valor_factura)
  elif opcion == 2:
    factura_a_eliminar = input("¿Qué factura deseas eliminar?: ")
    facturas_pendientes.pop(factura_a_eliminar)
  else:
    break

  print(f'Factua al momento: {facturas_pendientes}')
  falta_por_pagar = 0
  for factura in facturas_pendientes:
    falta_por_pagar += facturas_pendientes[factura]
  print(f'Aún queda ${falta_por_pagar} por pagar')