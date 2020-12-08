import pygame

class Bomb(): # Création de la casse de la bombe
    
    def __init__(self, skin, posx, posy, lenght, width,  power = 1):
        self.skin = skin
        self.x = posx
        self.y = posy
        self.lenght = lenght
        self.width = width
        self.power = power
        self.timer = 180

    def poseBomb(self, player, surface):
        bbombe_image = pygame.image.load(self.skin)
        surface.blit(bbombe_image, [self.x, self.y])

    def explosion(self):
        if self.timer > 0:
            self.timer -= 1
            print(self.timer)
        return self.timer