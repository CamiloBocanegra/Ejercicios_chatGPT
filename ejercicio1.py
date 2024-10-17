
def impares_inverso(inicio, fin):
    # Recorremos el rango de manera inversa
    for num in range(fin, inicio - 1, -1):
        if num % 2 != 0:  # Verificamos si el número es impar
            print(num)

# Ejemplo de uso
rango_min = int(input("introduzca el limite inferior del rango: "))
rango_max = int(input("introduzca el limite superior del rango: "))
impares_inverso(rango_min, rango_max)





