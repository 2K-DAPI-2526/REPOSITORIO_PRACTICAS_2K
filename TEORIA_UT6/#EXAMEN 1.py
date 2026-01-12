#genera programa para añadir, guardar y mostrar libros de una biblioteca en un fichero de texto
def aniadir_libros():
    with open("biblioteca.txt", "a") as fichero:
        while True:
            titulo = input("Introduce el título del libro (o 'salir' para terminar): ")
            if titulo.lower() == 'salir':
                break
            autor = input("Introduce el autor del libro: ")
            fichero.write(f"{titulo} - {autor}\n")
    print("Libros añadidos a la biblioteca.")

def mostrar_libros():
    try:
        with open("biblioteca.txt", "r") as fichero:
            print("Libros en la biblioteca:")
            for linea in fichero:
                print(linea.strip())
    except FileNotFoundError:
        print("No hay libros en la biblioteca.")

# Ejemplo de uso
aniadir_libros()
mostrar_libros()

#genera una funcion que permita 
