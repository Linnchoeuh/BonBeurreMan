import pygame
import includes.bomb as bomb
import includes.keyboard_input_detect as keyboard_input_detect
import includes.mapdisplayer as mapdisplayer

class Player():

    #Création caractéristiques principales joueur
    def __init__(self, sprite, pos_x, pos_y, length, width, unite, direction = 0):

        self.sprite = pygame.image.load(sprite)
        self.power = 2
        self.max_bomb = 1
        self.bomb_list = []

        self.x = pos_x
        self.y = pos_y
        self.length = length
        self.width = width
        self.maplimit = [0,0]
        self.centeringmap = [0,0]
        
        self.unite = unite

        self.look = direction
        self.frame_compensation = 0
        
    def vole_frame_compensation(self, machin): # C'est pour compenser les lags
        self.frame_compensation = machin

    def player_start(self, blockscale, playersspawns, centeringmapx, centeringmapy, maplimit):
        self.unite = blockscale
        self.x, self.y = (playersspawns[0]*blockscale)+centeringmapx, (playersspawns[1]*blockscale)+ centeringmapy
        self.sprite = pygame.transform.scale(self.sprite, (blockscale,blockscale))
        self.maplimit = [maplimit[0],maplimit[1]]
        self.centeringmap = [centeringmapx, centeringmapy]     
        print(self.maplimit)   
    
    
    def player_display(self, window_surface): # Fonction qui fait spawn le joueur
        window_surface.blit(self.sprite, (self.x,self.y))

    def set_bomb(self, surface): # Fonction qui fait spawn la bombe
        
        # if len(self.bomb_list) < self.max_bomb:
        #     self.bomb_list.append("yep")
        #     newBomb = bomb.Bomb("img/power_up/bombUp.png", self.x, self.y, 32, 32, self.power)
        #     newBomb.poseBomb(surface)
        #     newBomb.explosion(self.frame_compensation)            
        # else:
        #     pass

    # Movement du joueur
    def movement(self, dico_kb__inputs_bool, collisions, lag):
        lag -= 1
        # (longueur map x + 1) * (position du joueur y - (décalage pour centrer la carte y / taille d'un bloc) + ((position du joueur x - décalage pour centrer la carte x) / taille d'un bloc))
        #Bouge vers le haut
        if dico_kb__inputs_bool["z"] and lag <= 0 and collisions[(int((self.maplimit[0]+1)*(((self.y-self.unite)-self.centeringmap[1])/self.unite)+((self.x-self.centeringmap[0])/self.unite)))] == 0:
            self.y -= self.unite
            lag = 5
        
        #Bouge vers le bas
        if dico_kb__inputs_bool["s"] and lag <= 0 and collisions[(int((self.maplimit[0]+1)*(((self.y+self.unite)-self.centeringmap[1])/self.unite)+((self.x-self.centeringmap[0])/self.unite)))] == 0:
            self.y += self.unite
            lag = 5
        
        #Bouge vers la gauche
        if dico_kb__inputs_bool["q"] and lag <= 0 and collisions[(int((self.maplimit[0]+1)*((self.y-self.centeringmap[1])/self.unite)+(((self.x-self.unite)-self.centeringmap[0])/self.unite)))] == 0:
            self.x -= self.unite
            lag = 5
        
        #Bouge vers la droite
        if dico_kb__inputs_bool["d"] and lag <= 0 and collisions[(int((self.maplimit[0]+1)*((self.y-self.centeringmap[1])/self.unite)+(((self.x+self.unite)-self.centeringmap[0])/self.unite)))] == 0:
            self.x += self.unite
            lag = 5
    
        return lag
        
        

    # c'est pour avoir la direction que le joueur regarde
    # jsp où le mettre, d'ailleur jsp mm pas si ça va servir mais oklm c pg

    def direction(self, l_destination, l_depart):

        #Direction points
        dp = lambda destination, depart : destination - depart

        dir_dev_joueur = ""

        dir_x = dp(l_destination[0], l_depart[0])
        dir_y = dp(l_destination[1], l_depart[1])

        dir_l_xy = [dir_x, dir_y]
        
        dir_l_x = dir_l_xy[0]
        dir_l_y = dir_l_xy[1]

        if dir_l_x == 0 and dir_l_y < 0:
            dir_dev_joueur = "UP"
            
        if dir_l_x == 0 and dir_l_y > 0:
            dir_dev_joueur = "DOWN"
        
        if dir_l_x < 0 and dir_l_y == 0:
            dir_dev_joueur = "LEFT"
        
        if dir_l_x > 0 and dir_l_y == 0:
            dir_dev_joueur = "RIGHT"

        return dir_dev_joueur

    def track_coord(self, liste_maplimit, collisions):
        # 0 = ground
        # 1 = block solid
        # 2 = block breakable
        # 3 = wall
        # 4 = power-up

        surround_player = {
            "on" : False,
            "nord" : False,
            "sud" : False,
            "ouest" : False,
            "est" : False
        }
        
        x_limite, y_limite = liste_maplimit
        
        nb_lignes = len(collisions) // y_limite
        nb_colonnes = len(collisions) // x_limite
        
        pos_x = self.x
        pos_y = self.y

        num_block_joueur = pos_y * x_limite + pos_x #Num Block du joueur
        
        num_block_nord = (pos_y - 1) * x_limite + pos_x         #Num Block au dessus joueur
        num_block_sud = (pos_y + 1) * x_limite + pos_x          #Num Block en dessous joueur
        num_block_ouest = pos_y * x_limite + (pos_x - 1)        #Num Block à gauche joueur
        num_block_est = pos_y * x_limite + (pos_x + 1)          #Num Block à droite joueur

    
        block_on = collisions[num_block_joueur]                 #Block du joueur

        block_nord = collisions[num_block_nord]                 #Block au dessus joueur
        block_sud = collisions[num_block_sud]                   #Block en dessous joueur
        block_ouest = collisions[num_block_ouest]               #Block à gauche joueur
        block_est = collisions[num_block_est]                   #Block à droite joueur

        type_collision = 1
        
        if block_on is type_collision:
            surround_player["on"] = True
        else:
            surround_player["on"] = False
        
        if block_nord is type_collision:
            surround_player["nord"] = True
        else:
            surround_player["nord"] = False
        
        if block_sud is type_collision:
            surround_player["sud"] = True
        else:
            surround_player["sud"] = False
        
        if block_ouest is type_collision:
            surround_player["ouest"] = True
        else:
            surround_player["ouest"] = False
        
        if block_ouest is type_collision:
            surround_player["est"] = True
        else:
            surround_player["est"] = False

        return surround_player