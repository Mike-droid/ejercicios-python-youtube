contactos = {}


menu = """
  Bienvenido al sistema de agenda. Digite el número de la acción que desea realizar:

  1. Registrar un contacto
  2. Ver lista de contactos
  3. Eliminar un contacto
  4. Cambiar el número de un contacto
  5. Salir
  """


def registar_contacto():
  nombre = input("Ingrese el nombre del contacto: ")
  telefono = input("Ingrese el teléfono del contacto: ")
  datos = {
    "nombre": nombre,
    "telefono": telefono
  }
  if len(contactos) == 0:
    contactos[nombre] = telefono
    print("Contacto registrado con éxito.")
  else:
    if telefono in contactos.values():
      print("Error, contacto duplicado.")
    else:
      contactos[nombre] = telefono
      print("Contacto registrado con éxito.")


def listar_contactos():
  for nombre, telefono in contactos.items():
    print(f"Nombre: {nombre}, Teléfono: {telefono}")
    print("------")


def eliminar_contacto():
  contacto_a_eliminar = input("Ingrese el nombre del contacto que desea eliminar: ")
  if contacto_a_eliminar in contactos.keys():
    contactos.pop(contacto_a_eliminar)
    print("Contacto eliminado con éxito.")
  else:
    print("Error, contacto no encontrado.")


def cambiar_numero_contacto():
  nombre_contacto = input("Ingrese el nombre del contacto que desea editar: ")
  if nombre_contacto not in contactos.keys():
    print("Error, contacto no encontrado.")
  for nombre, telefono in contactos.items():
    if nombre == nombre_contacto:
      telefono_nuevo = input("Ingrese el nuevo teléfono: ")
      contactos[nombre] = telefono_nuevo
      print("Contacto editado con éxito.")


def sistema():
  print(menu)
  while True:
    opcion = input("Digite una opción: ")
    if opcion == "1":
      registar_contacto()
    elif opcion == "2":
      listar_contactos()
    elif opcion == "3":
      eliminar_contacto()
    elif opcion == "4":
      cambiar_numero_contacto()
    elif opcion == "5":
      print("Programa finalizado. Gracias por utilizar el sistema de agenda.")
      break
    else:
      print("Opción incorrecta. Inténtalo nuevamente.")


if __name__ == '__main__':
  sistema()
