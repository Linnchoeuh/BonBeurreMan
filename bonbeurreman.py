from os import system
try:
    import pygame
except:
    print("Erreur pygame n'est pas installé.")
    print("Installation automatique...")
    print("Mise à jour de pip...")
    system("python -m pip install --upgrade pip")
    print("Installation de pygame...")
    system("pip install pygame")
    print("Pip à été mis à jour et pygame a été installé.\nSi le programme ne se lance toujours pas, faite manuellement les installations\nPour installer voici la marche à suivre:\nPremièrement faites 'windows+r', tapez 'cmd' et appuyer sur entré.\n Nous allons d'abbord vérifier que pip est à jour, entrez la commande si dessous dans l'invite de commande que vous avez ouvert:\npython -m pip install --upgrade pip\nAttendez la fin de l'instalation et entrez ensuite cette commande pour installer pygame:\npip install pygame\n Une fois l'installation terminé vous devriez pouvoir lancer correctement ce programme\n Appuyez sur entrée pour continuer.")
    import pygame

import includes.player as player
import includes.bomb as bomb
import includes.mapdisplayer as mapdisplayer
import ctypes
from os import listdir
from os.path import isfile, join


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

fichiers = [f for f in listdir("levels") if isfile(join("levels", f))] #Liste les niveau stocké dans le dossier levels, et seulement ceux finissant par .data
temp = []
for i in range(len(fichiers)):
    if fichiers[i].find(".data") != -1:
        temp.append(fichiers[i][:fichiers[i].find(".data")])
fichiers = temp
# print(fichiers)

md = mapdisplayer.Mapdislayer()
result = "ok"

# key_name = [
#     "K_z",
#     "K_s",
#     "K_q",
#     "K_d",
#     "K_UP",
#     "K_DOWN",
#     "K_LEFT",
#     "K_RIGHT",
#     "K_SPACE",
#     "K_LSHIFT",
#     "K_RETURN",
#     "K_ESCAPE"
# ]
    
# Génération des fonctions -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def update_fps(): # Permet de voir les fps
    window_surface.blit(fps_text.render(str(round(clock.get_fps(), 2)), False, red), res_pos(10,10))

def res_pos(spacex = 0, spacey = 0): # Permet de positionner un élement au meme endroit peu importe la résolution d'affichage
    return round(spacex * res[0]/1920) , round(spacey * res[1]/1080)

def res_adaptation(height):
    return round(height * res[1]/1080)

def collision_rect(x, y, width, height, text = False, click_block_condition = False): # Permet de creer une zone de collision (position x, position y, largeur, hauteur, texte(facultatif), 
    pressed = False                                                                   # empêcher l'activation du boutton si le click gauche de la souris est déjà pressé
    touched = False                                                                   # (mettre la variable mouse_click_left)(par défaut actif))
    if mx >= res_pos(x)[0] and my >= res_pos(0,y)[1] and mx <= res_pos(x+width)[0] and my <= res_pos(0,y+height)[1]:
        touched = True
        if mousepress[0] and mouse_click_left == True or mousepress[0] and click_block_condition == True:
            pressed = True
    if text != False:
        window_surface.blit(text_40a.render(text, True, white), res_pos(x+res_pos(15)[0],y+((res_pos(0,height-50)[1])/2)))
    if devmode == True:
        pygame.draw.rect(window_surface, white, pygame.Rect(res_pos(x)[0], res_pos(0,y)[1], res_pos(width)[0], res_pos(0,height)[1]), 1)

    return (touched, pressed)

pygame.init() # Lancement de pygame -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

clock = pygame.time.Clock()

pygame.display.set_caption("BonBeurreMan") # Renommer l'intitulé de la fenêtre

window_surface = pygame.display.set_mode(res)

#Chargement des polices d'écritures
fps_text = pygame.font.Font(join("fonts", "VCR_OSD_MONO_1.ttf"), round(res_adaptation(33))) # Autres
text_40a = pygame.font.Font(join("fonts", "arialbd.ttf"), round(res_adaptation(60)))
text_150a = pygame.font.Font(join("fonts", "arialbd.ttf"), round(res_adaptation(150)))

#Chargement des textures
warn = pygame.image.load(f"img/ui/warn.png").convert_alpha() #Fonction pour importe l'image
warn = pygame.transform.smoothscale(warn, res_pos(220,200)) #N'utiliser pas smooth scale sur une pixel art car ca la rendrait flou
# warn = pygame.transform.scale(warn, res_pos(220,200)) #Fonction pour la scale a la résolution d'affichage





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
    # print(keyboard_input)
    window_surface.fill(black)
    
    if menu == 0: #Menu principal -------------------------------------------------------------------------------------------------------------------------------------------------------------
        if load_menu != 0: # Mettez ici les éléments a charger une seule fois
            mouse_click_left = False
            load_menu = 0
        if collision_rect(810, 375, 300, 150, "Jouer")[1] == True:
            menu = 1
        if collision_rect(810, 600, 300, 150, "Options")[1] == True:
            # menu = 2
            pass
        if collision_rect(810, 825, 300, 150, "Quitter")[1] == True:
            launched = False
    
    if menu == 1: #Selection du niveau --------------------------------------------------------------------------------------------------------------------------------------------------------
        if load_menu != 1: # Mettez ici les éléments a charger une seule fois
            mouse_click_left = False
            load_menu = 1
        
        window_surface.blit(text_150a.render("Choisissez votre niveau", True, white), res_pos(60,0))

        for i in range(len(fichiers)):
            if collision_rect(100+(i*325), 300, 265, 300, f"{fichiers[i]}")[1] == True:
                result = md.load(fichiers[i])
                if result == "Invalid extension" or result == "Corrupted map":
                    menu = 2
        
        if collision_rect(0, 975, 300, 105, "Retour")[1] == True:
            menu = 0
        if collision_rect(1320, 975, 600, 105, "Connecter manettes")[1] == True:
            pass
        if collision_rect(490, 975, 675, 105, "Connexion multi local")[1] == True:
            pass
    
    if menu == 2:
        window_surface.blit(warn, res_pos(850,100))
        if result == "Invalid extension":
            window_surface.blit(text_40a.render("Le fichier n'as pas pu être chargé car il est inexistant", True, red), res_pos(195,450))  
            window_surface.blit(text_40a.render("ou son extension ne fini pas par '.data'.", True, red), res_pos(360,525))
        else:
            window_surface.blit(text_40a.render("Le fichier n'as pas pu être chargé", True, red), res_pos(480,450))
            window_surface.blit(text_40a.render("car ce n'est pas une carte de jeu pour BonBeurreMan", True, red), res_pos(200,525))
        if collision_rect(0, 975, 300, 105, "Retour")[1] == True:
            menu = 1


    # print(collision_rect(50 ,50, 50, 50, "oui"))
    
    if mousepress[0] == 1:
        mouse_click_left = False
    else:
        mouse_click_left = True


    




    update_fps() # Affiche les fps
    pygame.display.flip() # Met a jour l'affichage
    dt = clock.tick(60)/1500 # Permet de limiter la framerate a 60fps
