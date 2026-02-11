#Bienvenidos a la clase de programación orientada a objetos. En esta clase, vamos a crear un juego de rol simple utilizando clases y objetos en Python. El juego consistirá en personajes que pueden atacar, defenderse y subir de nivel. Cada personaje tendrá atributos como fuerza, vida, nivel, puntería, magia, resistencia, velocidad e inteligencia.

class personaje:
    
    def __init__(self, nombre, fuerza, vida=100, nivel=1,punteria=100,magia=100,resistencia=100,velocidad=100,inteligencia=100):    
        self.nombre = nombre
        self.fuerza = fuerza
        self.vida = vida
        self.nivel = nivel
        self.punteria = punteria
        self.magia = magia
        self.resistencia = resistencia
        self.velocidad = velocidad
        self.inteligencia = inteligencia
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
        self.punteria += self.punteria * 0.05
        self.magia += self.magia * 0.05
        self.resistencia += self.resistencia * 0.05
        self.velocidad += self.velocidad * 0.05
        self.inteligencia += self.inteligencia * 0.05
        print(f"{self.nombre} ha subido al nivel {self.nivel}. Fuerza: {self.fuerza}, Vida: {self.vida}, Puntería: {self.punteria}, Magia: {self.magia}, Resistencia: {self.resistencia}, Velocidad: {self.velocidad}, Inteligencia: {self.inteligencia}")

    def mostrar_vida(self):
        print(f"{self.nombre} tiene {self.vida} de vida.")


# Ejemplo de uso
#Si el guerrero derrota a un enemigo, sube de nivel y mejora sus habilidades.
#Si la vida del guerrero llega a cero, no puede atacar ni defenderse.
#cuando el guerrero ataca, el daño causado se calcula multiplicando su fuerza por su nivel, y se resta de la vida del enemigo.
#cuando el un guerrero ataca a otro, si el enemigo ya está derrotado, no se puede atacar.
#Cada vez que un guerrero ataca y el otro se defiende, el guerrero defensor recupera vida en función de su fuerza.
#cuando un guerrero ataca a otro, se deben mostrar las vidas de ambos guerreros después del ataque.
#Ambos guerreros comienzan con 100 de vida, pero pueden aumentar su vida al subir de nivel o al defenderse.
#Cada guerrero tiene un nombre único y una clase
