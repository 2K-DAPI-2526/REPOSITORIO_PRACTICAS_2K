#Creame un fichero de alumnos con nombre, nota media y si ha aprobado o no.
with open("alumnos.txt", "a") as fichero:
   fichero.write(f"Nombre: Gorka,  Media: 6.8, Aprobado: Si\n")
   fichero.write(f"Nombre: Ana,  Media: 5.4, Aprobado: Si\n")
   fichero.write(f"Nombre: Luis,  Media: 4.2, Aprobado: No\n")
   fichero.write(f"Nombre: Marta,  Media: 7.1, Aprobado: Si\n")
   fichero.write(f"Nombre: Carlos,  Media: 3.9, Aprobado: No\n")

#quiero que aparexca el fichero de alumnos completo por pantalla 
with open("alumnos.txt", "r") as fichero: 
    contenido = fichero.read()
    print(contenido)

#Como accedo a los elementos de un fichero linea a linea
with open("alumnos.txt", "r") as fichero:
      for linea in fichero:
         print(linea.strip())

#Como accedo a una URL y muestro su contenido por pantalla
import requests
url = "http://example.com"
response = requests.get(url)
print(response.text)




