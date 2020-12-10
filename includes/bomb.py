import pygame

class Bomb(): # Création de la casse de la bombe
    
    def __init__(self, sprite, posx, posy, lenght, width, power = 2):
        self.sprite = pygame.image.load(sprite)
        self.x = posx
        self.y = posy
        self.lenght = lenght
        self.width = width
        self.power = power
        self.timer = 190

    def poseBomb(self, surface, bomb_index):
        if bomb_index != []:
            for i in range(len(bomb_index)):   
                
                surface.blit(self.sprite, [self.x, self.y])

    def explosion(self, dt):
        if self.timer > 10:
            self.timer -= dt*60
            print(self.timer)
            return self.timer
        self.sprite = "img/texture/explo.png"
        if self.timer > 0:           
            self.timer -= dt*60
            return self.timer
        