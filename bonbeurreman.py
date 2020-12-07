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
# res = [640, 360]
mx = 0 # Definition de la position x de la souris
my = 0 # Definition de la position y de la souris
mousepress = [0,0,0] # Permet d'acceder au input de la souris, sachant que mousepress[0] = click gauche, mousepress[1] = click molette, mousepress[2] = click droit
devmode = True
menu = 0 #Menu d'entrée
load_menu = 0 #Variable permettant de charger a la première frame du menu actif

mouse_click_left = True # Variable a utiliser si l'on veut que l'utilisateur relache le click
keyboard_input = {
    "z" : False,
    "s" : False,
    "q" : False,
    "d" : False,
    "UP" : False,
    "DOWN" : False,
    "LEFT" : False,
    "RIGHT" : False,
    "SPACE" : False,
    "LSHIFT" : False,
    "RETURN" : False,
    "ESCAPE" : False
} #Dictionnaire des touches pressables

key_name = [
    "K_z",
    "K_s",
    "K_q",
    "K_d",
    "K_UP",
    "K_DOWN",
    "K_LEFT",
    "K_RIGHT",
    "K_SPACE",
    "K_LSHIFT",
    "K_RETURN",
    "K_ESCAPE"
]
    
# Génération des fonctions -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def update_fps(): # Permet de voir les fps
    window_surface.blit(fps_text.render(str(round(clock.get_fps(), 2)), False, red), res_pos(5,5))

def res_pos(spacex = 0, spacey = 0): # Permet de positionner un élement au meme endroit peu importe la résolution d'affichage
    return (spacex/1280) * res[0] , (spacey/720) * res[1]

def res_adaptation(height):
    return height * res[1]//720

def collision_rect(x, y, width, height, text = False, click_block_condition = False): # Permet de creer une zone de collision (position x, position y, largeur, hauteur, texte(facultatif), 
    pressed = False                                                                   # empêcher l'activation du boutton si le click gauche de la souris est déjà pressé
    touched = False                                                                   # (mettre la variable mouse_click_left)(par défaut actif))
    if mx >= res_adaptation(x) and my >= res_adaptation(y) and mx <= res_adaptation(x+width) and my <= res_adaptation(y+height):
        touched = True
        if mousepress[0] and mouse_click_left == True or mousepress[0] and click_block_condition == True:
            pressed = True
    if text != False:
        window_surface.blit(text_40a.render(text, True, white), res_pos(x+res_adaptation(10),y+((height-res_adaptation(50))/2)))
    if devmode == True:
        pygame.draw.rect(window_surface, white, pygame.Rect(res_adaptation(x), res_adaptation(y), res_adaptation(width), res_adaptation(height)), 1)

    return (touched, pressed)

pygame.init() # Lancement de pygame -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

pygame.display.set_caption("BonBeurreMan") # Renommer l'intitulé de la fenêtre


fps_text = pygame.font.Font(os.path.join("fonts", "VCR_OSD_MONO_1.ttf"), round(res_adaptation(22))) # Autres
text_40a = pygame.font.Font(os.path.join("fonts", "arialbd.ttf"), round(res_adaptation(40)))

clock = pygame.time.Clock()

window_surface = pygame.display.set_mode(res)
launched = True
while launched: # Pour fermer la fenêtre
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            launched = False
    
    pressing = pygame.key.get_pressed()
    
    #z
    if pressing[pygame.K_z]:
        keyboard_input["z"] = True
    else:
        keyboard_input["z"] = False
        

    #s
    if pressing[pygame.K_s]:
        keyboard_input["s"] = True
    else:
        keyboard_input["s"] = False
        

    #q
    if pressing[pygame.K_q]:
        keyboard_input["q"] = True
    else:
        keyboard_input["q"] = False
        

    #d
    if pressing[pygame.K_d]:
        keyboard_input["d"] = True
    else:
        keyboard_input["d"] = False
        

    #UP
    if pressing[pygame.K_UP]:
        keyboard_input["UP"] = True
    else:
        keyboard_input["UP"] = False
        

    #DOWN
    if pressing[pygame.K_DOWN]:
        keyboard_input["DOWN"] = True
    else:
        keyboard_input["DOWN"] = False
        

    #LEFT
    if pressing[pygame.K_LEFT]:
        keyboard_input["LEFT"] = True
    else:
        keyboard_input["LEFT"] = False
        

    #RIGHT
    if pressing[pygame.K_RIGHT]:
        keyboard_input["RIGHT"] = True
    else:
        keyboard_input["RIGHT"] = False
        

    #SPACE
    if pressing[pygame.K_SPACE]:
        keyboard_input["SPACE"] = True
    else:
        keyboard_input["SPACE"] = False
        

    #LSHIFT
    if pressing[pygame.K_LSHIFT]:
        keyboard_input["LSHIFT"] = True
    else:
        keyboard_input["LSHIFT"] = False
        

    #RETURN
    if pressing[pygame.K_RETURN]:
        keyboard_input["RETURN"] = True
    else:
        keyboard_input["RETURN"] = False
        

    #ESCAPE
    if pressing[pygame.K_ESCAPE]:
        keyboard_input["ESCAPE"] = True
    else:
        keyboard_input["ESCAPE"] = False
    
    mx, my = pygame.mouse.get_pos()
    mousepress = pygame.mouse.get_pressed()
    print(keyboard_input)
    window_surface.fill(black)
    if menu == 0: #Menu principal
        if load_menu != 0: # Mettez ici les éléments a charger une seule fois
            mouse_click_left = False
            load_menu = 0
        if collision_rect(540, 250, 200, 100, "Jouer")[1] == True:
            menu = 1
    if menu == 1: #Selection du niveau
        if load_menu != 1: # Mettez ici les éléments a charger une seule fois
            mouse_click_left = False
            load_menu = 1
        if collision_rect(0, 650, 200, 70, "Retour")[1] == True:
            menu = 0
        if collision_rect(880, 650, 400, 70, "Connecter manettes")[1] == True:
            pass


    # print(collision_rect(50 ,50, 50, 50, "oui"))
    
    if mousepress[0] == 1:
        mouse_click_left = False
    else:
        mouse_click_left = True


    




    update_fps() # Affiche les fps
    pygame.display.flip() # Met a jour l'affichage
    dt = clock.tick(60)/1000 # Permet de limiter la framerate a 60fps
