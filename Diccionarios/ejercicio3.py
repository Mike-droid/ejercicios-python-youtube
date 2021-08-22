frutas = {
  'plátano' : 1.35,
  'manzana' : 0.80,
  'pera' : 0.85,
  'naranja' : 0.70
}

fruta = input("¿Qué fruta deseas?: ")

if fruta in frutas:
  kilos = float(input(f"¿Cuántos kilos de {fruta} quieres?: "))
  print(f"{kilos} kilos de {fruta} cuestan ${frutas[fruta]*kilos}")
else:
  print(f"{fruta} no se encuentra disponible 😥")