import pygame

class Player():

    #Création caractéristiques principales joueur
    def __init__(self, sprite, set_bomb, tt, power_up_audio):

        self.originalsprite = pygame.image.load(sprite)
        self.sprite = 0
        self.power = 2 # power up
        self.max_bomb = 1 # bombe up
        self.bomb_list = []

        self.x = 0
        self.y = 0
        self.coords = [self.x, self.y]
        self.maplimit = [0,0]
        self.centeringmap = [0,0]
        
        self.unite = 0
        self.frame_compensation = 0
        self.cd = 0
        self.bomb_up = 1
        self.lag = 0
        self.lag_temp = 6 #speed up
        self.player_id = 0

        self.set_bomb_sound = pygame.mixer.Sound(set_bomb)
        self.set_bomb_sound.set_volume(0.75)

        self.tt_song = pygame.mixer.Sound(tt)
        self.tt_song.set_volume(0.5)

        self.pwr_up_sfx = pygame.mixer.Sound(power_up_audio)
        self.pwr_up_sfx.set_volume(0.5)

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

    def set_bomb(self, collision_updater, oenable, bomb_data): # Fonction qui fait spawn la bombe
        n = 0
        for number in self.bomb_list: # Vérifie si certaines bombes n'ont pas déja explosée
            if number <= 0:
                self.bomb_list.pop(n) # et si oui, les supprime
            n += 1
        if len(self.bomb_list) < self.max_bomb: # Vérifie si on a pas posé toute les bombes disponibles
            self.bomb_list.append(100)
            if oenable == False:
                self.set_bomb_sound.play()
            else:
                self.tt_song.play()
            collision_updater.append([int((self.maplimit[0]+1)*((self.y-self.centeringmap[1])/self.unite)+((self.x-self.centeringmap[0])/self.unite)), 3])
            bomb_data.append([self.x, self.y, 100])
        return bomb_data, collision_updater
        

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

    def bonus_checker(self,powerup_data):   
        try:     
            for i in range(len(powerup_data)):
                if self.x == powerup_data[i][1][0] and self.y == powerup_data[i][1][1]: # CA CA BUG je comprend pas pk

                    if powerup_data[i][0] == 0: # speed up
                        if self.lag_temp > 3:
                            self.lag_temp -= 0.5
                            self.pwr_up_sfx.play()


                    elif powerup_data[i][0] == 1: # power up
                        self.power += 1
                        self.pwr_up_sfx.play()

                    elif powerup_data[i][0] == 2: # bomb up
                        self.max_bomb += 1
                        self.pwr_up_sfx.play()

                    powerup_data.pop(i) # le bonus ca dégage
        except:
            print("oh le bug")
            pass