#---------------- IMPORTS ----------------
#importar librerías de pygames desde consola: 
# <py -m pip install pygame>
import pygame
# ---------------- CONFIGURACIÓN ----------------
resolution = (800, 600)

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

# ---------------- CLASE BALL ----------------
class Ball:
    def __init__(self, xPos=None, yPos=None, xVel=2, yVel=2, rad=15):
        self.x = xPos if xPos else resolution[0] / 2
        self.y = yPos if yPos else resolution[1] / 2
        self.dx = xVel
        self.dy = yVel
        self.radius = rad
        self.type = "ball"
        self.timer = pygame.time.get_ticks()

    def draw(self, surface):
        pygame.draw.circle(surface, black, (int(self.x), int(self.y)), self.radius)

    def update(self, gameObjects):
        self.x += self.dx
        self.y += self.dy

        if self.x <= self.radius or self.x >= resolution[0] - self.radius:
            self.dx *= -1
        if self.y <= self.radius or self.y >= resolution[1] - self.radius:
            self.dy *= -1

        # Reducir velocidad cada 7.5 segundos
        now = pygame.time.get_ticks()
        if now - self.timer > 7500:
            self.timer = now
            self.dx *= 0.9
            self.dy *= 0.9


# ---------------- CLASE PLAYER ----------------
class Player:
    def __init__(self, rad=20):
        self.x = resolution[0] / 2
        self.y = resolution[1] / 2
        self.dx = 0
        self.dy = 0
        self.radius = rad
        self.type = "player"

    def draw(self, surface):
        pygame.draw.circle(surface, red, (int(self.x), int(self.y)), self.radius)

    def update(self, gameObjects):
        keys = pygame.key.get_pressed()
        speed = 3

        if keys[pygame.K_LEFT]:
            self.x -= speed
        if keys[pygame.K_RIGHT]:
            self.x += speed
        if keys[pygame.K_UP]:
            self.y -= speed
        if keys[pygame.K_DOWN]:
            self.y += speed

        # Colisión con la pelota
        for gameObj in gameObjects:
            if gameObj.type == "ball":
                dist = (gameObj.x - self.x) ** 2 + (gameObj.y - self.y) ** 2
                if dist <= (gameObj.radius + self.radius) ** 2:
                    if keys[pygame.K_SPACE]:
                        gameObj.dx = self.dx if self.dx != 0 else gameObj.dx
                        gameObj.dy = self.dy if self.dy != 0 else gameObj.dy


# ---------------- CLASE GAME ----------------
class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(resolution)
        pygame.display.set_caption("Juego con Ball y Player")
        self.clock = pygame.time.Clock()
        self.gameObjects = [Ball(), Player()]

    def handleEvents(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

    def run(self):
        while True:
            self.handleEvents()

            for obj in self.gameObjects:
                obj.update(self.gameObjects)

            self.screen.fill(white)

            for obj in self.gameObjects:
                obj.draw(self.screen)

            pygame.display.flip()
            self.clock.tick(60)


# ---------------- EJECUCIÓN ----------------
Game().run()

#---------------- FIN DEL CÓDIGO ----------------
