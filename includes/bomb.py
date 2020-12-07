import pygame

class Bomb(): # Création de la casse de la bombe
    
    def __init__(self, skin, posx, posy, lenght, width,  power = 1):
        self.skin = skin
        self.posx = posx
        self.posy = posy
        self.lenght = lenght
        self.width = width
        self.power = power

    def explosion(self, klok, timer):
        clock = klok.tick(60)/1000
        
        if timer > 0:
            timer -= 1