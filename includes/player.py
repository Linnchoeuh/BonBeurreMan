import pygame
import includes.bomb as bomb
import includes.keyboard_input_detect as keyboard_input_detect

#Taille Unité du carreau 32px
TILESIZE = 32

class Player():

    #Création caractéristiques principales joueur
    def __init__(self, sprite, pos_x, pos_y, length, width, speed, direction = 0):
        
        self.sprite = sprite
        self.x = pos_x
        self.y = pos_y
        self.length = length
        self.width = width
        self.speed = speed
        self.direction = direction

        self.position_actuelle = [self.x,self.y]
        self.position_preced = self.position_actuelle
        self.position_nouv = [self.x,self.y] # Modif [self.x + preshot_x, self.y + preshot_y]


    def spawn_player(self, windows_surface):
        player_sprite = pygame.image.load(self.sprite)
        return pygame.surface.blit(player_sprite, self.position_actuelle)


    #Movement du joueur
    #def movement(self):
    #    
    #    #Bouge vers le haut
    #    if keyboard_input["z"]:
    #        self.y -= TILESIZE
    #    
    #    #Bouge vers le bas
    #    if keyboard_input["s"]:
    #        self.y += TILESIZE
    #    
    #    #Bouge vers la gauche
    #    if keyboard_input["q"]:
    #        self.x -= TILESIZE
    #    
    #    #Bouge vers la droite
    #    if keyboard_input["d"]:
    #        self.x += TILESIZE  

    # c'est pour avoir la direction que le joueur regarde
    # jsp où le mettre, d'ailleur jsp mm pas si ça va servir mais oklm c pg
    def direction(l_destination, l_depart):

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