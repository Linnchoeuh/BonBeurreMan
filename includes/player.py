import pygame

class Player():

    #Création caractéristiques principales joueur
    def __init__(self, sprite, set_bomb, tt):

        self.originalsprite = pygame.image.load(sprite)
        self.sprite = 0
        self.power = 2
        self.max_bomb = 1
        self.bomb_list = []

        self.x = 0
        self.y = 0
        self.maplimit = [0,0]
        self.centeringmap = [0,0]
        
        self.unite = 0
        self.frame_compensation = 0
        self.cd = 0
        self.lag = 0
        self.lag_temp = 3
        self.player_id = 0

        self.set_bomb_sound = pygame.mixer.Sound(set_bomb)
        self.set_bomb_sound.set_volume(0.75)

        self.tt_song = pygame.mixer.Sound(tt)
        self.tt_song.set_volume(0.5)

    def player_start(self, blockscale, playersspawns, centeringmapx, centeringmapy, maplimit, player_id):
        self.unite = blockscale
        self.x, self.y = (playersspawns[0]*blockscale)+centeringmapx, (playersspawns[1]*blockscale)+ centeringmapy
        self.sprite = pygame.transform.scale(self.originalsprite, (1000,1000))
        if blockscale >= 32:    
            self.sprite = pygame.transform.scale(self.sprite, (blockscale,blockscale))
        else:
            self.sprite = pygame.transform.smoothscale(self.sprite, (blockscale,blockscale))
        self.maplimit = [maplimit[0],maplimit[1]]
        self.centeringmap = [centeringmapx, centeringmapy]     
        self.player_id = player_id
        # print(self.maplimit)   
    
    
    def player_display(self, window_surface, frame_compensation, show): # Fonction qui fait spawn le joueur
        if show == True:   
            window_surface.blit(self.sprite, (self.x,self.y))
            if self.cd > 0:
                self.cd -= 1*frame_compensation

    def set_bomb(self, collision_updater, oenable): # Fonction qui fait spawn la bombe
        if self.cd <= 0:
            if oenable == False:
                self.set_bomb_sound.play()
            else:
                self.tt_song.play()
            self.cd = 100
            collision_updater.append([int((self.maplimit[0]+1)*((self.y-self.centeringmap[1])/self.unite)+((self.x-self.centeringmap[0])/self.unite)), 3])
            return [self.x, self.y, 100], collision_updater
        return "none", collision_updater
        

    # Movement du joueur
    def movement(self, dico_kb__inputs_bool, collisions, frame_compensation):
        self.lag -= 1*frame_compensation
        # (longueur map x + 1) * (position du joueur y - (décalage pour centrer la carte y / taille d'un bloc) + ((position du joueur x - décalage pour centrer la carte x) / taille d'un bloc))
        # print(collisions[(int((self.maplimit[0]+1)*((self.y-self.centeringmap[1])/self.unite)+((self.x-self.centeringmap[0])/self.unite)))])
        #Bouge vers le haut
        if dico_kb__inputs_bool["z"] and self.lag <= 0 and collisions[(int((self.maplimit[0]+1)*(((self.y-self.unite)-self.centeringmap[1])/self.unite)+((self.x-self.centeringmap[0])/self.unite)))] == 0:
            self.y -= self.unite
            self.lag = self.lag_temp
        
        #Bouge vers le bas
        if dico_kb__inputs_bool["s"] and self.lag <= 0 and collisions[(int((self.maplimit[0]+1)*(((self.y+self.unite)-self.centeringmap[1])/self.unite)+((self.x-self.centeringmap[0])/self.unite)))] == 0:
            self.y += self.unite
            self.lag = self.lag_temp
        
        #Bouge vers la gauche
        if dico_kb__inputs_bool["q"] and self.lag <= 0 and collisions[(int((self.maplimit[0]+1)*((self.y-self.centeringmap[1])/self.unite)+(((self.x-self.unite)-self.centeringmap[0])/self.unite)))] == 0:
            self.x -= self.unite
            self.lag = self.lag_temp
        
        #Bouge vers la droite
        if dico_kb__inputs_bool["d"] and self.lag <= 0 and collisions[(int((self.maplimit[0]+1)*((self.y-self.centeringmap[1])/self.unite)+(((self.x+self.unite)-self.centeringmap[0])/self.unite)))] == 0:
            self.x += self.unite
            self.lag = self.lag_temp
        
    def movementp2(self, dico_kb__inputs_bool, collisions, frame_compensation):
        self.lag -= 1*frame_compensation
        # (longueur map x + 1) * (position du joueur y - (décalage pour centrer la carte y / taille d'un bloc) + ((position du joueur x - décalage pour centrer la carte x) / taille d'un bloc))
        #Bouge vers le haut
        if dico_kb__inputs_bool["UP"] and self.lag <= 0 and collisions[(int((self.maplimit[0]+1)*(((self.y-self.unite)-self.centeringmap[1])/self.unite)+((self.x-self.centeringmap[0])/self.unite)))] == 0:
            self.y -= self.unite
            self.lag = self.lag_temp
        
        #Bouge vers le bas
        if dico_kb__inputs_bool["DOWN"] and self.lag <= 0 and collisions[(int((self.maplimit[0]+1)*(((self.y+self.unite)-self.centeringmap[1])/self.unite)+((self.x-self.centeringmap[0])/self.unite)))] == 0:
            self.y += self.unite
            self.lag = self.lag_temp
        
        #Bouge vers la gauche
        if dico_kb__inputs_bool["LEFT"] and self.lag <= 0 and collisions[(int((self.maplimit[0]+1)*((self.y-self.centeringmap[1])/self.unite)+(((self.x-self.unite)-self.centeringmap[0])/self.unite)))] == 0:
            self.x -= self.unite
            self.lag = self.lag_temp
        
        #Bouge vers la droite
        if dico_kb__inputs_bool["RIGHT"] and self.lag <= 0 and collisions[(int((self.maplimit[0]+1)*((self.y-self.centeringmap[1])/self.unite)+(((self.x+self.unite)-self.centeringmap[0])/self.unite)))] == 0:
            self.x += self.unite
            self.lag = self.lag_temp

    def kill(self, collisions, endgame):
        if collisions[(int((self.maplimit[0]+1)*((self.y-self.centeringmap[1])/self.unite)+((self.x-self.centeringmap[0])/self.unite)))] == 4:
            endgame[self.player_id-1] = False
        return endgame