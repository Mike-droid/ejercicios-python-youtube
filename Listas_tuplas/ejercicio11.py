v1 = (1,-2,3)
v2 = (-1,6,2)

#* (1,2,3) * (-1,0,2) = [1 * -1] + [2 * 0] + [3 * 2] = [-1 + 0 + 6] = 5

producto_escalar = 0

for i in range(len(v1)):
  producto_escalar += v1[i] * v2[i]

print(f'El producto escalar de {v1} * {v2} = {producto_escalar}')