cesta = {}

menu = """
1. Agregar producto
2. Salir y pagar
"""

while True:
  print(menu)
  opcion = int(input("¿Qué deseas hacer?: "))

  if opcion == 1:
    producto_nuevo = input("Inserta el nombre del producto: ")
    precio_nuevo = float(input("Inserta el precio del producto: "))
    nuevo = cesta.setdefault(producto_nuevo , precio_nuevo)
    print(cesta)
  else:
    total = 0
    for producto in cesta:
      total += cesta[producto]
    print(f"Total a pagar ${total}")
    break