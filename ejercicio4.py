

def imprimir_piramide_invertida():
    for i in range(9, 0, -2):  # Comienza con 6 estrellas en la fila superior
        espacios = " " * (9 - i)  # Agrega espacios al principio para centrar el patrón
        estrellas = "* " * i  # Imprime las estrellas con un espacio entre ellas
        print(espacios + estrellas)

# Llamada a la función
imprimir_piramide_invertida()
