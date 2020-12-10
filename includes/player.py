import pygame
import includes.bomb as bomb
import includes.keyboard_input_detect as keyboard_input_detect
import includes.mapdisplayer as mapdisplayer

class Player():

    #Création caractéristiques principales joueur
    def __init__(self, sprite, pos_x, pos_y, length, width, unite, direction = 0):
        
        self.sprite = pygame.image.load(sprite)
        self.power = 2
        self.x = pos_x
        self.y = pos_y
        self.length = length
        self.width = width
        
        self.unite = md.blockscale

        self.direction = direction
        self.frame_compensation = 1

        self.position_actuelle = [self.x,self.y]
        self.position_preced = self.position_actuelle
        self.position_nouv = [self.x,self.y] # Modif [self.x + preshot_x, self.y + preshot_y]
        
    def vole_frame_compensation(self, machin): # C'est pour compenser les lags
        self.frame_compensation = machin

    def spawn_player(self, window_surface): # Fonction qui fait spawn le joueur
        return window_surface.blit(self.sprite, self.position_actuelle)

    def spawn_bomb(self, bomb, surface): # Fonction qui fait spawn la bombe
        newBomb = bomb.Bomb("img/power_up/bombUp.png", self.x, self.y, 32, 32, self.power)
        newBomb.poseBomb(surface)
        newBomb.explosion(self.frame_compensation)


    # Movement du joueur
    def movement(self):
       
       #Bouge vers le haut
       if keyboard_input["z"]:
           self.y -= self.unite
       
       #Bouge vers le bas
       if keyboard_input["s"]:
           self.y += self.unite
       
       #Bouge vers la gauche
       if keyboard_input["q"]:
           self.x -= self.unite
       
       #Bouge vers la droite
       if keyboard_input["d"]:
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

