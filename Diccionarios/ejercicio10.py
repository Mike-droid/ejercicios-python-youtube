base_de_datos = {}

menu = """
(1) Añadir cliente
(2) Eliminar cliente
(3) Mostrar cliente
(4) Listar todos los clientes
(5) Listar clientes preferentes
(6) Terminar
"""

while True:
  print(menu)
  opcion = int(input("¿Qué deseas hacer?: "))

  if opcion == 1:
    NIF = int(input("NIF: "))
    nombre = input("Nombre: ")
    direccion = input("Dirección: ")
    telefono = input("Teléfono: ")
    correo = input("Correo: ")
    preferente = input("¿Preferente? (s/n): ")
    datos = {
      'nombre': nombre,
      'direccion': direccion,
      'telefono': telefono,
      'correo': correo,
      'preferente': preferente == 's'
    }
    base_de_datos.setdefault(NIF , datos)

  elif opcion == 2:
    cliente_a_eliminar = int(input("¿Qué cliente deseas eliminar?: "))
    base_de_datos.pop(cliente_a_eliminar)

  elif opcion == 3:
    cliente = int(input("¿De qué cliente deseas saber su información?: "))
    if cliente in base_de_datos:
      print(base_de_datos[cliente])
    else:
      print("El cliente no existe")

  elif opcion == 4:
    print(base_de_datos)

  elif opcion == 5:
    for clave , valor in base_de_datos.items():
      if valor['preferente']:
        print(clave,valor)

  else:
    break