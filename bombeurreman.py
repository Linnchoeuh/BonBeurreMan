import os
try:
    import pygame
except:
    print("Erreur pygame n'est pas installé.")
    print("Installation automatique...")
    print("Mise à jour de pip...")
    os.system("python -m pip install --upgrade pip")
    print("Installation de pygame...")
    os.system("pip install pygame")
    print("Pip à été mis à jour et pygame a été installé.\nSi le programme ne se lance toujours pas, faite manuellement les installations\nPour installer voici la marche à suivre:\nPremièrement faites 'windows+r', tapez 'cmd' et appuyer sur entré.\n Nous allons d'abbord vérifier que pip est à jour, entrez la commande si dessous dans l'invite de commande que vous avez ouvert:\npython -m pip install --upgrade pip\nAttendez la fin de l'instalation et entrez ensuite cette commande pour installer pygame:\npip install pygame\n Une fois l'installation terminé vous devriez pouvoir lancer correctement ce programme\n Appuyez sur entrée pour continuer.")
    import pygame

import includes.player
import includes.bomb
import ctypes   

# Definitions des variables -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

red = (255, 0, 0) # Quelque variable de couleur prédéfini
green = (0, 255, 0)
blue = (0, 0, 255)
magenta = (255, 0, 255)
yellow = (255, 255, 0)
cyan = (0, 255, 255)
white = (255,255,255)
light_gray = (225, 225, 225)
gray = (150,150,150)
dark_gray = (75, 75, 75)
black = (0, 0, 0)

res = [1280, 720] # Definition de la résolution d'affichage
mx = 0 # Definition de la position x de la souris
my = 0 # Definition de la position y de la souris
mousepress = [0,0,0] # Permet d'acceder au input de la souris, sachant que mousepress[0] = click gauche, mousepress[1] = click molette, mousepress[2] = click droit

mouse_click_left = True # Variable a utiliser si l'on veut que l'utilisateur relache le click
    
# Génération des fonctions -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def update_fps(): # Permet de voir les fps
    window_surface.blit(fps_text.render(str(round(clock.get_fps(), 2)), False, red), res_pos(5,5))

def res_pos(spacex = 0, spacey = 0): # Permet de se positionner au meme endroit peu importe la résolution d'affichage
    return round((spacex/1920) * res[0]) , round((spacey/1080) * res[1])

def res_adaptation(height):
    return round(height * res[1]/720)

def collision_rect(x, y, width, height): # Permet de creer une zone de collision
    if mx >= x and my >= y and mx <= x+width and my <= y+height:
        print("oui")
        if mousepress[0] and mouse_click_left == False:
            return True
    return False

pygame.init() # Lancement de pygame -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

pygame.display.set_caption("BonBeurreMan") # Renommer l'intitulé de la fenêtre


fps_text = pygame.font.Font(os.path.join("fonts", "VCR_OSD_MONO_1.ttf"), round(res_adaptation(22))) # Autres
text_40a = pygame.font.Font(os.path.join("fonts", "arialbd.ttf"), round(res_adaptation(40)))

clock = pygame.time.Clock()

carre = pygame.Rect(res_adaptation(725),res_adaptation(550),res_adaptation(30),res_adaptation(30))

window_surface = pygame.display.set_mode(res)
launched = True
while launched: # Pour fermer la fenêtre
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            launched = False
    
    mx, my = pygame.mouse.get_pos()
    mousepress = pygame.mouse.get_pressed()
    
    window_surface.fill(black)
    
    window_surface.blit(text_40a.render("yo", True, white), res_pos(50,50))
    collision_rect(50, 50, 50, 50)
    pygame.draw.rect(window_surface, white, carre)
    
    update_fps() # Affiche les fps
    pygame.display.flip() # Met a jour l'affichage
    dt = clock.tick(60)/1000 # Permet de limiter la framerate a 60fps
