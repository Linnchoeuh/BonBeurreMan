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
        del_bomb_list = []
        if bomb_index != []:
            for i in range(len(bomb_index)):   
                surface.blit(self.sprite, [bomb_index[i][0], bomb_index[i][1]])
                bomb_index[i][2] -= 1
                if bomb_index[i][2] <= 0:
                    del_bomb_list.append(i)
        if del_bomb_list != []:
            for i in range(len(del_bomb_list)):
                del bomb_index[del_bomb_list[i]]

        
        return bomb_index


    def explosion(self, dt):
        if self.timer > 10:
            self.timer -= dt*60
            print(self.timer)
            return self.timer
        self.sprite = "img/texture/explo.png"
        if self.timer > 0:           
            self.timer -= dt*60
            return self.timer
        