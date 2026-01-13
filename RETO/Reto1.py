#Escribir un programa que guarde en un fichero la secuencia de tableros de una partida de ajedrez.
#Partiremos del tablero inicial donde las filas del tablero 
#El programa debe guardar el tablero inicial en un fichero con el nombre que elija el usuario. 
#Después debe preguntar al usuario si quiere hacer un movimiento o terminar la partida. Cada 
#vez que el usuario quiera hacer un nuevo movimiento debe preguntar la fila y la columna de la 
#pieza que quiere mover y la fila y la columna a la que la quiere mover. Tras ello añadirá el 
#tablero resultante al final del fichero anterior.

def crear_tablero_inicial():
    tablero = [
        ["r", "n", "b", "q", "k", "b", "n", "r"],
        ["p", "p", "p", "p", "p", "p", "p", "p"],
        [".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", "."],
        ["P", "P", "P", "P", "P", "P", "P", "P"],
        ["R", "N", "B", "Q", "K", "B", "N", "R"]
    ]
    return tablero

def guardar_tablero_en_fichero(tablero, nombre_fichero):
    with open(nombre_fichero, 'a') as f:
        for fila in tablero:
            f.write(' '.join(fila) + '\n')
        f.write('\n')  # Separador entre tableros
        
def mostrar_tablero(tablero):
    for fila in tablero:
        print(' '.join(fila))
    print()  # Línea en blanco para separar tableros

def mover_pieza(tablero, fila_origen, col_origen, fila_destino, col_destino):
    pieza = tablero[fila_origen][col_origen]
    tablero[fila_origen][col_origen] = "."
    tablero[fila_destino][col_destino] = pieza

def main():
    nombre_fichero = input("Introduce el nombre del fichero para guardar la partida: ")
    tablero = crear_tablero_inicial()
    guardar_tablero_en_fichero(tablero, nombre_fichero)
    mostrar_tablero(tablero)

    while True:
        accion = input("¿Quieres hacer un movimiento (m) o terminar la partida (t)? ").lower()
        if accion == 't':
            print("Partida terminada.")
            break
        elif accion == 'm':
            try:
                fila_origen = int(input("Fila de la pieza a mover (0-7): "))
                col_origen = int(input("Columna de la pieza a mover (0-7): "))
                fila_destino = int(input("Fila destino (0-7): "))
                col_destino = int(input("Columna destino (0-7): "))

                mover_pieza(tablero, fila_origen, col_origen, fila_destino, col_destino)
                guardar_tablero_en_fichero(tablero, nombre_fichero)
                mostrar_tablero(tablero)
            except (ValueError, IndexError):
                print("Movimiento inválido. Inténtalo de nuevo.")
        else:
            print("Opción no válida. Por favor, elige 'm' o 't'.")

#no se mueve nada, no se si funciona
#la funcion de mover pieza creo que no funciona
if __name__ == "__main__":
    main()
#no se mueve nada, no se si funciona
#la funcion de mover pieza creo que no funciona
#no se mueve nada, no se si funciona
#la funcion de mover pieza creo que no funciona
#no se mueve nada, no se si funciona
#como juego una partida?
#debería preguntar si quiero mover o no
