nombre = input("Escribe tu nombre: ")
edad = input("Escribe tu edad: ")
direccion = input("Escribe tu dirección: ")
telefono = input("Escribe tu número de teléfono: ")

datos_usuario = {
  'nombre' : nombre,
  'edad' : edad,
  'direccion' : direccion,
  'telefono' : telefono
}

print(f"{datos_usuario['nombre']} tiene {datos_usuario['edad']} años, vive en {datos_usuario['direccion']} y su número de teléfono es {datos_usuario['telefono']}")