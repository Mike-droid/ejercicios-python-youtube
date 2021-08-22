edad = int(input("Escribe tu edad, por favor: "))
precio_entrada = 0.0

if edad < 4:
    print("¡Tienes entrada gratis!")
elif edad >= 4 and edad <= 18:
    precio_entrada = 5.0
    print(f"El precio por entrar es de ${precio_entrada}")
else:
    precio_entrada = 10.0
    print(f"El precio por entrar es de  ${precio_entrada}")