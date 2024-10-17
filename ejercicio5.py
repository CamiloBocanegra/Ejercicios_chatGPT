
def imprimir_rombo():
    # Parte superior del rombo
    for i in range(1, 10, 2):  # Comienza con 1 estrella y va hasta 9
        espacios = " " * (9 - i)  # Agrega espacios al principio para centrar el patrón
        estrellas = "* " * i  # Imprime las estrellas con un espacio entre ellas
        print(espacios + estrellas)

    # Parte inferior del rombo
    for i in range(7, 0, -2):  # Comienza con 7 estrellas y va hacia abajo
        espacios = " " * (9 - i)  # Agrega espacios al principio para centrar el patrón
        estrellas = "* " * i  # Imprime las estrellas con un espacio entre ellas
        print(espacios + estrellas)

# Llamar a la función para imprimir el rombo
imprimir_rombo()
