#Genera un fichero de nombres con numeros de teléfono
#!/usr/bin/env python3
def generar_fichero_nombres_telefonos(nombre_fichero, num_registros):
    import random

    nombres = ["Ana", "Luis", "Carlos", "Marta", "Sofía", "Javier", "Lucía", "David", "Elena", "Pablo"]
    with open(nombre_fichero, 'w') as fichero:
        for _ in range(num_registros):
            nombre = random.choice(nombres)
            telefono = f"{random.randint(600000000, 699999999)}"
            fichero.write(f"{nombre},{telefono}\n")
    print(f"Fichero '{nombre_fichero}' generado con {num_registros} registros.")
    