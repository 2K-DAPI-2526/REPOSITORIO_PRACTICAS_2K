import Definicion_personajes  

#Definición de clases: Cada clase, tendrá los atributos que comparten la clase personajes y además ganarán un atributo por pertenecer a esa clase.
#Si eres arquero, tienes un 10% más de puntería y un 10% más de velocidad
#Si eres guerrero, tienes un 10% más de fuerza  y un 10% más de resistencia
#Si eres mago, tienes un 10% más de magia y un 10% más de inteligencia
#Si eres ladrón, tienes un 10% más de velocidad y un 10% más de inteligencia
#todos comienzan con los atributos propios de la clase personaje, pero cada clase tiene un atributo adicional que mejora en un 10% al pertenecer a esa clase.
#Todas las calses comienzan con los atributos propios a esa clase.
#Si el personaje sube de nivel, mejora sus atributos en un 5% adicional.

#-------------VAMOS A DEFINIR LAS CLASES-----------------#

class guerrero(Definicion_personajes.personaje):
    def __init__(self, nombre, fuerza, vida=100, nivel=1, resistencia=0):
        super().__init__(nombre, fuerza, vida, nivel)
        self.resistencia = resistencia * 1.1  # Aumento del 10% por ser guerrero

class arquero(Definicion_personajes.personaje):
    def __init__(self, nombre, fuerza, velocidad, vida =100, punteria = 100):
        super().__init__(nombre, fuerza, vida, nivel=1)
        self.punteria = punteria * 1.1  # Aumento del 10% por ser arquero
        self.velocidad = velocidad * 1.1  # Aumento del 10% por ser arquero

class mago(Definicion_personajes.personaje):
    def __init__(self, nombre, fuerza, vida =100, magia = 100):
        super().__init__(nombre, fuerza, vida, nivel=1)
        self.magia = magia * 1.1  # Aumento del 10% por ser mago

class ladron(Definicion_personajes.personaje):
    def __init__(self, nombre, fuerza, velocidad, vida =100, inteligencia = 100):
        super().__init__(nombre, fuerza, vida, nivel=1)
        self.velocidad = velocidad * 1.1  # Aumento del 10% por ser ladrón
        self.inteligencia = inteligencia * 1.1  # Aumento del 10% por ser ladrón


#Una vez definidas las clases, podemos crear personajes de cada clase y probar sus habilidades. Por ejemplo:
guerrero1 = guerrero("Thor", 20, 10)
arquero1 = arquero("Legolas", 15, 20)
mago1 = mago("Gandalf", 10, 15)
ladron1 = ladron("Garrett", 12, 18)
guerrero1.atacar(arquero1)
arquero1.mostrar_vida()
arquero1.atacar(guerrero1)
guerrero1.mostrar_vida()
mago1.atacar(ladron1)
ladron1.mostrar_vida()
ladron1.atacar(mago1)
