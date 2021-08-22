password = input("Escribe tu contraseñan: ")
contrasena = "Tesla"

#! bucle while
while password != contrasena:
    intento = input("Contraseña incorrecta, por favor intenta de nuevo: ")
    if intento == contrasena:
        print("Bienvenido")
        break