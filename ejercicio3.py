
def crear_matriz():
    matriz = []
    for i in range(6):
        fila = [1 if j <= i else 0 for j in range(6)]
        matriz.append(fila)
    
    # Imprimir la matriz
    for fila in matriz:
        print(fila)

# Llamada a la función
crear_matriz()