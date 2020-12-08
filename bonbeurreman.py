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
    input("Pip à été mis à jour et pygame a été installé.\nSi le programme ne se lance toujours pas, faite manuellement les installations\nPour installer voici la marche à suivre:\nPremièrement faites 'windows+r', tapez 'cmd' et appuyer sur entré.\n Nous allons d'abbord vérifier que pip est à jour, entrez la commande si dessous dans l'invite de commande que vous avez ouvert:\npython -m pip install --upgrade pip\nAttendez la fin de l'instalation et entrez ensuite cette commande pour installer pygame:\npip install pygame\n Une fois l'installation terminé vous devriez pouvoir lancer correctement ce programme\n Appuyez sur entrée pour continuer.")
    import pygame

# import includes.player as player
import includes.bomb as bomb
import includes.mapdisplayer as mapdisplayer
import includes.keyboard_input_detect as keyboard_input_detect
import ctypes
from os import listdir
from os.path import isfile, join


# Definitions des variables -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# player1 = Player()

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
# keyboard_input = KeyBoardKeyDetect.keyboard_input_fonc() 
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

fichiers = [f for f in listdir("levels") if isfile(join("levels", f))] #Liste les niveaux stocké dans le dossier levels, et seulement ceux qui contiennent .data dans leur nom
temp = []
for i in range(len(fichiers)):
    if fichiers[i].find(".data") != -1:
        temp.append(fichiers[i][:fichiers[i].find(".data")])
fichiers = temp
# print(fichiers)

md = mapdisplayer.Mapdislayer(res)
result = "ok"
level_select_offset = 0
pause = False
escape_released = True
bb = False
    
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

def collision_rect_texture(x, y, texture, texture_rect, click_block_condition = False): # Permet de creer une zone de collision avec une image fixe(position x, position y, texture, sa zone de collisions,
    pressed = False                                                     # empêcher l'activation du boutton si le click gauche de la souris est déjà pressé
    window_surface.blit(texture, res_pos(x,y))
    # print(texture_rect.collidepoint(mx,my))
    if mousepress[0] and mouse_click_left == True and texture_rect.collidepoint(mx,my) == 1 or mousepress[0] and click_block_condition == True and texture_rect.collidepoint(mx,my) == 1:
        pressed = True
    # if devmode == True:
    #     pygame.draw.rect(window_surface, white, pygame.Rect(res_pos(x)[0], res_pos(0,y)[1], res_pos(width)[0], res_pos(0,height)[1]), 1)
    return pressed

pygame.init() # Lancement de pygame -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
print("Jeu réalisé par Tony, Jean-Pierre, Kimi et Lenny")

clock = pygame.time.Clock()

pygame.display.set_caption("BonBeurreMan") # Renommer l'intitulé de la fenêtre

# window_surface = pygame.display.set_mode(res, pygame.FULLSCREEN)
window_surface = pygame.display.set_mode(res)


#Chargement des polices d'écritures
fps_text = pygame.font.Font(join("fonts", "VCR_OSD_MONO_1.ttf"), round(res_adaptation(33))) # Autres
text_40a = pygame.font.Font(join("fonts", "arialbd.ttf"), round(res_adaptation(60)))
text_150a = pygame.font.Font(join("fonts", "arialbd.ttf"), round(res_adaptation(150)))

window_surface.blit(text_150a.render("Chargement...", True, white), res_pos(450,425))
pygame.display.flip()

#Chargement des textures
warn = pygame.image.load(f"img/ui/warn.png").convert_alpha() #Fonction pour importer l'image
warn = pygame.transform.smoothscale(warn, res_pos(220,200)) #N'utiliser pas smooth scale sur une pixel art car ca le rendrait flou
# warn = pygame.transform.scale(warn, res_pos(220,200)) #Fonction pour la scale a la résolution d'affichage

left_arrow = pygame.image.load(f"img/ui/left_arrow.png").convert_alpha()
left_arrow = pygame.transform.smoothscale(left_arrow, res_pos(95,180))

right_arrow = pygame.image.load(f"img/ui/right_arrow.png").convert_alpha()
right_arrow = pygame.transform.smoothscale(right_arrow, res_pos(95,180))

ground = pygame.image.load(f"img/map/ground.png").convert_alpha()
block = pygame.image.load(f"img/map/block.png").convert_alpha()
break_block = pygame.image.load(f"img/map/break_block.png").convert_alpha()
wall = pygame.image.load(f"img/map/wall.png").convert_alpha()





launched = True
while launched: # Pour fermer la fenêtre
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            launched = False
    
    keyboard_input = keyboard_input_detect.keyboard_input_fonc(pygame)
    # print(keyboard_input)
    
    mx, my = pygame.mouse.get_pos() #Position de la souris
    mousepress = pygame.mouse.get_pressed() #Vérifie si un bouton de la souris est appuyé
    
    window_surface.fill(black)
    
    if menu == 0: #Menu principal -------------------------------------------------------------------------------------------------------------------------------------------------------------
        if load_menu != 0: # Mettez ici les éléments a charger une seule fois
            mouse_click_left = False
            load_menu = 0
        if collision_rect(810, 375, 300, 150, "Jouer")[1] == True: #Passe sur le menu de selection de niveau
            menu = 1
            level_select_offset = 0
        if collision_rect(810, 600, 300, 150, "Options")[1] == True: #Passe sur les options
            menu = 2
        if collision_rect(810, 825, 300, 150, "Quitter")[1] == True: #Ferme le jeu
            launched = False
    
    if menu == 1: #Selection du niveau --------------------------------------------------------------------------------------------------------------------------------------------------------
        if load_menu != 1: # Mettez ici les éléments a charger une seule fois
            mouse_click_left = False
            left_arrow_rect = left_arrow.get_rect(topleft=res_pos(25,350))
            right_arrow_rect = right_arrow.get_rect(topleft=res_pos(1800,350))
            load_menu = 1
        
        window_surface.blit(text_150a.render("Choisissez votre niveau", True, white), res_pos(60,0))

        if level_select_offset*5 < len(fichiers)-1:
            if collision_rect_texture(1800, 360, right_arrow, right_arrow_rect) == True:
                level_select_offset += 1
        if level_select_offset*5 >= 4:
            if collision_rect_texture(25, 360, left_arrow, left_arrow_rect) == True:
                level_select_offset -= 1



        k = i = level_select_offset*5
        if i < 0:
            i = 0
        while i <= k+4: #Affiche la selection des niveaux
            if i+1 > len(fichiers):
                break
            if collision_rect(160+i*325-k*325, 300, 265, 300, f"{fichiers[i]}")[1] == True: #Si un niveau est activé
                window_surface.fill(black)
                window_surface.blit(text_150a.render("Chargement...", True, white), res_pos(450,425))
                pygame.display.flip()
                result = md.load(fichiers[i], res, pygame, ground, block, break_block, wall) #Chargement du niveau selectionné
                if result == "Invalid extension" or result == "Corrupted map":
                    menu = 10
                else:
                    menu = 3
            i += 1
        
        if menu != 3:
            if collision_rect(0, 975, 300, 105, "Retour")[1] == True:
                menu = 0
            if collision_rect(1320, 975, 600, 105, "Connecter manettes")[1] == True:
                pass
            if collision_rect(490, 975, 675, 105, "Connexion multi local")[1] == True:
                pass
    
    if menu == 2: #Options --------------------------------------------------------------------------------------------------------------------------------------------------------
        if load_menu != 2: # Mettez ici les éléments a charger une seule fois
            mouse_click_left = False
            load_menu = 2
        if collision_rect(0, 975, 300, 105, "Retour")[1] == True:
            menu = 0    
    
    if menu == 3:
        if load_menu != 3: # Mettez ici les éléments a charger une seule fois
            mouse_click_left = False
            load_menu = 3
        

        md.displayer(window_surface, warn)
        

        #if keyboard_input["SPACE"] == True:
        #    bb = True
        #    timer = 180

        #if bb == True:            
        #    if timer > 0:
        #        poseBomb()
        #        timer -= dt*70 # ????
        #    else:
        #        bb = False
        #        timer = 180
        
        
        
        
        if escape_released == True: #Activation de la pause
            if pause == False and keyboard_input["ESCAPE"] == True:
                escape_released = False
                pause = True
            elif keyboard_input["ESCAPE"] == True:
                escape_released = False
                pause = False
        
        if keyboard_input["ESCAPE"] == True:
            escape_released = False
        else:
            escape_released = True

        if pause == True:
            window_surface.blit(text_150a.render("Pause", True, white), res_pos(720,0))
            if collision_rect(790, 500, 300, 105, "Continuer")[1] == True:
                pause = False
            if collision_rect(530, 700, 825, 105, "Retour au choix des niveaux")[1] == True:
                menu = 1
                pause = False

                

    if menu == 10:
        window_surface.blit(warn, res_pos(850,100))
        if result == "Invalid extension":
            window_surface.blit(text_40a.render("Le fichier n'as pas pu être chargé car il est inexistant", True, red), res_pos(195,450))  
            window_surface.blit(text_40a.render("ou son extension ne fini pas par '.data'.", True, red), res_pos(360,525))
        else:
            window_surface.blit(text_40a.render("Le fichier n'as pas pu être chargé", True, red), res_pos(480,450))
            window_surface.blit(text_40a.render("car ce n'est pas une carte de jeu pour BonBeurreMan", True, red), res_pos(200,525))
        if collision_rect(0, 975, 300, 105, "Retour")[1] == True:
            menu = 1
    
    if mousepress[0] == 1:
        mouse_click_left = False
    else:
        mouse_click_left = True

    #Vérifie le click gauche


    update_fps() # Affiche les fps
    pygame.display.flip() # Met a jour l'affichage
    dt = clock.tick(60)/1000 # Permet de limiter la framerate a 60fps
