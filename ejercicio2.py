
def impares_inverso(inicio, fin):
   impares = []
   for num in range(fin, inicio - 1, -1):
      if num % 2 != 0:
         impares.append(str(num))  # Agregamos el número a la lista como cadena de texto
   print(", ".join(impares))  # Imprimimos la lista de impares unida por comas

rango_min = int(input("introduzca el limite inferior del rango: "))
rango_max = int(input("introduzca el limite superior del rango: "))
impares_inverso(rango_min, rango_max)