datos_usuario = {}

menu = """
1. Agregar datos
2. Salir
"""

while True:
  print(menu)
  opcion = int(input("¿Qué quieres hacer?: "))

  if opcion == 1:
    clave_nueva = input("Inserta una clave nueva: ")
    valor_nuevo = input("Inserta un valor nuevo: ")
    nuevo = datos_usuario.setdefault(clave_nueva , valor_nuevo)
    print(datos_usuario)
  else:
    break
