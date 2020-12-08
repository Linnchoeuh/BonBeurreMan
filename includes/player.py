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


    def spawn_player(self, windows_surface):
        pass

        


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