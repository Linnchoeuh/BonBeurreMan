import pygame
import includes.bomb as bomb
import includes.keyboard_input_detect as keyboard_input_detect
import includes.mapdisplayer as mapdisplayer

class Player():

    #Création caractéristiques principales joueur
    def __init__(self, sprite, pos_x, pos_y, length, width, unite, direction = 0):

        self.sprite = sprite
        self.power = 2
        self.max_bomb = 1
        self.bomb_list = []

        self.x = pos_x
        self.y = pos_y
        self.length = length
        self.width = width
        
        self.unite = unite

        self.direction = direction

        self.position_actuelle = [self.x,self.y]
        self.position_preced = self.position_actuelle
        self.position_nouv = [self.x,self.y] # Modif [self.x + preshot_x, self.y + preshot_y]
        
    def vole_frame_compensation(machin,self): # C'est pour compenser les lags
        self.frame_compensation = machin


    def spawn_player(self, window_surface): # Fonction qui fait spawn le joueur
        return window_surface.blit(self.sprite, self.position_actuelle)

    def spawn_bomb(self, bomb, surface): # Fonction qui fait spawn la bombe
        if len(self.bomb_list) < self.max_bomb:
            self.bomb_list.append(yep)
            newBomb = bomb.Bomb("img/power_up/bombUp.png", self.x, self.y, 32, 32, self.power)
            newBomb.poseBomb(surface)
            newBomb.explosion(self.frame_compensation)            
        else:
            pass

    # Movement du joueur
    def movement(self, dico_kb__inputs_bool):
       
       #Bouge vers le haut
       if dico_kb__inputs_bool["z"]:
           self.y -= self.unite
       
       #Bouge vers le bas
       if dico_kb__inputs_bool["s"]:
           self.y += self.unite
       
       #Bouge vers la gauche
       if dico_kb__inputs_bool["q"]:
           self.x -= self.unite
       
       #Bouge vers la droite
       if dico_kb__inputs_bool["d"]:
           self.x += self.unite

    # c'est pour avoir la direction que le joueur regarde
    # jsp où le mettre, d'ailleur jsp mm pas si ça va servir mais oklm c pg

    def direction(self, l_destination, l_depart):

        #Direction points
        dp = lambda destination, depart : destination - depart

        dir_dev_joueur = ""

        dir_x = dp(l_destination[0], l_depart[0])
        dir_y = dp(l_destination[1], l_depart[1])

        dir_l = [dir_x, dir_y]
        
        dir_l_x = dir_l[0]
        dir_l_y = dir_l[1]

        if dir_l_x == 0 and dir_l_y < 0:
            dir_dev_joueur = "UP"
            
        if dir_l_x == 0 and dir_l_y > 0:
            dir_dev_joueur = "DOWN"
        
        if dir_l_x < 0 and dir_l_y == 0:
            dir_dev_joueur = "LEFT"
        
        if dir_l_x > 0 and dir_l_y == 0:
            dir_dev_joueur = "RIGHT"

        return dir_dev_joueur

