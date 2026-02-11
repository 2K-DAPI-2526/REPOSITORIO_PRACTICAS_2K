class guerrero:
    def __init__(self, nombre, fuerza, vida=100, nivel=1):
        self.nombre = nombre
        self.fuerza = fuerza
        self.vida = vida
        self.nivel = nivel

    def atacar(self, enemigo):
        if self.vida <= 0:
            print(f"{self.nombre} no puede atacar porque está derrotado.")
            return

        if enemigo.vida <= 0:
            print(f"{enemigo.nombre} ya está derrotado.")
            return

        daño = self.fuerza * self.nivel
        enemigo.vida -= daño
        print(f"{self.nombre} ataca a {enemigo.nombre} causando {daño} de daño.")

        if enemigo.vida <= 0:
            enemigo.vida = 0
            print(f"{enemigo.nombre} ha sido derrotado por {self.nombre}.")
    
    def defenderse (self):
        if self.vida <= 0:
            print(f"{self.nombre} no puede defenderse porque está derrotado.")
            return

        defensa = self.fuerza * 0.5
        self.vida += defensa
        print(f"{self.nombre} se defiende y recupera {defensa} de vida.")

    def subir_nivel(self):
        self.nivel += 1
        self.fuerza += 5
        self.vida += 20
        print(f"{self.nombre} ha subido al nivel {self.nivel}. Fuerza: {self.fuerza}, Vida: {self.vida}")

    def mostrar_vida(self):
        print(f"{self.nombre} tiene {self.vida} de vida.")
        
# Ejemplo de uso
#Si el guerrero derrota a un enemigo, sube de nivel y mejora sus habilidades.
#Si la vida del guerrero llega a cero, no puede atacar ni defenderse.
guerrero1 = guerrero("Thor", 20)
guerrero2 = guerrero("Loki", 15)
guerrero1.atacar(guerrero2)
guerrero2.defenderse()
guerrero1.subir_nivel()
guerrero1.atacar(guerrero2)
guerrero2.atacar(guerrero1)
guerrero2.atacar(guerrero1)
guerrero1.defenderse()
guerrero1.atacar(guerrero2)
guerrero1.atacar(guerrero2)