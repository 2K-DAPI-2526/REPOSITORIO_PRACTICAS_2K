#Creame un fichero de alumnos con nombre, nota media y si ha aprobado o no.
with open("alumnos.txt", "a") as fichero:
   fichero.write(f"Nombre: Gorka,  Media: 6.8, Aprobado: Si\n")
   fichero.write(f"Nombre: Ana,  Media: 5.4, Aprobado: Si\n")
   fichero.write(f"Nombre: Luis,  Media: 4.2, Aprobado: No\n")
   fichero.write(f"Nombre: Marta,  Media: 7.1, Aprobado: Si\n")
   fichero.write(f"Nombre: Carlos,  Media: 3.9, Aprobado: No\n")

#hazme un algortimo para solicitar el nombre de un alumno y mostrar sus datos

with open("alumnos.txt", "r") as fichero:
   fichero.read()





