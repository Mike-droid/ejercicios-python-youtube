contrasena = "tesla"
password = input("¿Cuál es tu contraseña?: ") #TESLA

password = password.lower() #tesla
#password = password.upper() #TESLA

if contrasena == password: # = asignamos un valor , == preguntando si tienen el mismo valor
    print("Bienvenido")
else:
    print("contraseña incorrecta")