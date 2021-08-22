meses = {
  '1' : 'Enero',
  '2' : 'Febrero',
  '3' : 'Marzo',
  '4' : 'Abril',
  '5' : 'Mayo',
  '6' : 'Junio',
  '7' : 'Julio',
  '8' : 'Agosto',
  '9' : 'Septiembre',
  '10' : 'Octubre',
  '11' : 'Noviembre',
  '12' : 'Diciembre'
}

fecha = input("Escribe una fecha en formato dd/mmm/aaaa : ")
#* 22/10/2021
fecha = fecha.split("/")  #! fecha[dd][mmm][aaaa]
                          #! fecha[0][1][2]
print(f"{fecha[0]} / {meses[fecha[1]]} / {fecha[2]}")