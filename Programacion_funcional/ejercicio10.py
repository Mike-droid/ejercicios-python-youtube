def run():
  inmuebles = [
    {'año': 2000, 'metros': 100, 'habitaciones': 3, 'garaje': True, 'zona': 'A'}, # 0
    {'año': 2012, 'metros': 60, 'habitaciones': 2, 'garaje': True, 'zona': 'B'}, # 1
    {'año': 1980, 'metros': 120, 'habitaciones': 4, 'garaje': False, 'zona': 'A'}, # 2
    {'año': 2005, 'metros': 75, 'habitaciones': 3, 'garaje': True, 'zona': 'B'}, # 3
    {'año': 2015, 'metros': 90, 'habitaciones': 2, 'garaje': False, 'zona': 'A'} # 4
  ]

  precios = []
  year = 2021

  def calcula_precio_inmueble():
    for inmueble in inmuebles:
      for clave, valor in inmueble.items():
        if inmueble['zona'] == 'A':
          precio = (inmueble['metros'] * 1000 + inmueble['habitaciones'] * 5000 + inmueble['garaje'] * 15000) * (1-(year - inmueble['año'])/100)
        elif inmueble['zona'] == 'B':
          precio = (inmueble['metros'] * 1000 + inmueble['habitaciones'] * 5000 + inmueble['garaje'] * 15000) * (1-(year - inmueble['año'])/100) * 1.5
      precios.append(precio)
    return precios

  def busca_inmueble(presupuesto):
    print(f'Precios de los inmuebles {calcula_precio_inmueble()}')
    for precio in precios:
      if presupuesto >= precio:
        print(f'Puede comprar el apartamento de ${precio}\n')

  busca_inmueble(94000)

if __name__ == "__main__":
  run()
