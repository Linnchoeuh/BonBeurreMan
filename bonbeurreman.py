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
try:
    from PIL import Image
except:
    print("Erreur PIL n'est pas installé.")
    print("Installation automatique...")
    print("Mise à jour de pip...")
    system("python -m pip install --upgrade pip")
    print("Installation de PIL...")
    system("pip install pillow")
    input("Pip à été mis à jour et pil a été installé.\nSi le programme ne se lance toujours pas, faite manuellement les installations\nPour installer voici la marche à suivre:\nPremièrement faites 'windows+r', tapez 'cmd' et appuyer sur entré.\n Nous allons d'abbord vérifier que pip est à jour, entrez la commande si dessous dans l'invite de commande que vous avez ouvert:\npython -m pip install --upgrade pip\nAttendez la fin de l'instalation et entrez ensuite cette commande pour installer pygame:\npip install pillow\n Une fois l'installation terminé vous devriez pouvoir lancer correctement ce programme\n Appuyez sur entrée pour continuer.")
    from PIL import Image

import includes.player as player
import includes.bomb as bomb
import includes.mapdisplayer as mapdisplayer
import includes.keyboard_input_detect as keyboard_input_detect
import ctypes
from os import listdir
from os.path import isfile, join
import pickle

print("Jeu réalisé par Tony, Jean-Pierre, Kimi et Lenny")
print("Démarage de BonBeurreMan...")
# Definitions des variables -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
player1 = player.Player("img/power_up/powerUp.png", 10, 100, 32, 32, 5)
bbomb = bomb.Bomb("img/power_up/bombUp.png", player1.x, player1.y, 32, 32)

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

res = [1920, 1080] # Definition de la résolution d'affichage
# res = [640, 360]
mx = 0 # Definition de la position x de la souris
my = 0 # Definition de la position y de la souris
mousepress = [0,0,0] # Permet d'acceder au input de la souris, sachant que mousepress[0] = click gauche, mousepress[1] = click molette, mousepress[2] = click droit
devmode = False
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

referenced_minimap = ["none"]
try:
    with open(f"includes/properties/minimap_cache.data", "rb") as minimapfile:
        get_record = pickle.Unpickler(minimapfile)
        referenced_minimap = get_record.load()
except:
    with open(f"includes/properties/minimap_cache.data", "wb") as minimapfile:
        record = pickle.Pickler(minimapfile)
        record.dump(referenced_minimap)

minimap_list = []
tempfichiers = []
for b in range(len(fichiers)):
    founded = False
    check = False
    for k in range(len(referenced_minimap)):
        if fichiers[b] == referenced_minimap[k]:
            founded = True
            break
    # print(founded)
    if founded == False:
        try: #Détecte si le fichier a été suprimé, ou si le fichier ne fini pas par l'extension .data
            with open(f"levels/{fichiers[b]}.data", "rb") as lvl:
                get_record = pickle.Unpickler(lvl)
                try: #Detecte si le fichier n'est pas une liste
                    lvl_data = get_record.load()
                except:
                    pass
        except:
            pass
        try:
            if lvl_data[0] != "MapApprovedCertificate": #Vérifie que la map détient bien a l'occurence 0 le certificat "MapApprovedCertificate" qui permet de s'assurer que ce fichier est lisible en tant que map de jeu
                pass #Signale l'absence du certificat et retourne l'erreur comme quoi le fichier est corrompu
            else:
                check = True
                # print(f"Valid file : {fichiers[b]}")
        except:
            pass #Si la vérification du certificat echoue
            
        if check == True:
            maplimit = [lvl_data[1], lvl_data[2]] #Stocke la taille de la map
            mapcontent = lvl_data[4:] #Stocke les élement de la map
            temp = []
            for i in range(len(mapcontent)): #vérifie que la liste ne contient pas d'élément qui dépasse de la carte, et les retire le cas echeant
                if mapcontent[i][1] <= maplimit[0] and mapcontent[i][2] <= maplimit[1]:
                    temp.append(mapcontent[i])
            mapcontent = [] #trie et rempli les cases n'ayant pas été référencé par du sol
            for i in range(maplimit[1]+1):
                for k in range(maplimit[0]+1):
                    block_exist = False
                    for a in range(len(temp)):
                        if temp[a] == [temp[a][0], k, i]:
                            mapcontent.append(temp[a])
                            block_exist = True
                            break
                    if block_exist == False:
                        mapcontent.append([0, k, i])
            if 1/(maplimit[0]+1) < 1/(maplimit[1]+1):
                blockscale = 32*(maplimit[0]+1)
                centeringmapx = 0
                centeringmapy = int((32*(maplimit[0]+1))/2-(32*(maplimit[1]+1))/2)
            else:
                blockscale = 32*(maplimit[1]+1)
                centeringmapx = int((32*(maplimit[1]+1))/2-(32*(maplimit[0]+1))/2)
                centeringmapy = 0
            images = [Image.open(x) for x in ["img/map/ground.png", "img/map/block.png", "img/map/break_block.png", "img/map/wall.png"]]
            line = []
            total_width = blockscale
            max_height = 32
            for i in range(maplimit[1]+1):
                new_im = Image.new('RGB', (total_width, max_height))
                x_offset = centeringmapx
                for k in range(maplimit[0]+1):
                    # print(mapcontent[k])
                    new_im.paste(images[mapcontent[i*(maplimit[0]+1)+k][0]], (int(x_offset),0))
                    x_offset += 32
                line.append(new_im)

            max_height = blockscale
            new_im = Image.new('RGB', (total_width, max_height))
            y_offset = centeringmapy
            for i in range(len(line)):
                new_im.paste(line[i], (0,int(y_offset)))
                y_offset += 32

            new_im.save(f"img/temp/mini_map/{fichiers[b]}_cache.png")
            tempfichiers.append(fichiers[b])


fichiers = tempfichiers


md = mapdisplayer.Mapdislayer(res)
result = "ok"
level_select_offset = 0
pause = False
escape_released = True
bb = False
level_slide = 0
    
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
    pressed = False                                                                     # empêcher l'activation du boutton si le click gauche de la souris est déjà pressé
    window_surface.blit(texture, res_pos(x,y))                                          # (mettre la variable mouse_click_left)(par défaut actif))
    if mousepress[0] and mouse_click_left == True and texture_rect.collidepoint(mx,my) == 1 or mousepress[0] and click_block_condition == True and texture_rect.collidepoint(mx,my) == 1:
        pressed = True
    return pressed

pygame.init() # Lancement de pygame -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

clock = pygame.time.Clock()

pygame.display.set_caption("BonBeurreMan") # Renommer l'intitulé de la fenêtre

window_surface = pygame.display.set_mode(res, pygame.FULLSCREEN)
# window_surface = pygame.display.set_mode(res)


#Chargement des polices d'écritures
fps_text = pygame.font.Font(join("fonts", "VCR_OSD_MONO_1.ttf"), round(res_adaptation(33))) # Autres
text_40a = pygame.font.Font(join("fonts", "arialbd.ttf"), round(res_adaptation(60)))
text_150a = pygame.font.Font(join("fonts", "arialbd.ttf"), round(res_adaptation(150)))

window_surface.blit(text_150a.render("Chargement...", True, white), res_pos(450,425))
pygame.display.flip()

#Chargement des textures

s = pygame.Surface(res)  # the size of your rect
s.set_alpha(128)         # alpha level
s.fill((0, 0, 0))        # this fills the entire surface

for i in range(len(fichiers)):
    minimapimg = pygame.image.load(f"img/temp/mini_map/{fichiers[i]}_cache.png").convert_alpha()
    minimapimg = pygame.transform.smoothscale(minimapimg, res_pos(265,265))
    minimap_list.append(minimapimg)

warn = pygame.image.load(f"img/ui/warn.png").convert_alpha() #Fonction pour importer l'image
warn = pygame.transform.smoothscale(warn, res_pos(220,200)) #N'utiliser pas smooth scale sur une pixel art car ca le rendrait flou
# warn = pygame.transform.scale(warn, res_pos(220,200)) #Fonction pour la scale a la résolution d'affichage

left_arrow = pygame.image.load("img/ui/left_arrow.png").convert_alpha()
left_arrow = pygame.transform.smoothscale(left_arrow, res_pos(95,180))

right_arrow = pygame.image.load("img/ui/right_arrow.png").convert_alpha()
right_arrow = pygame.transform.smoothscale(right_arrow, res_pos(95,180))

ground = pygame.image.load("img/map/ground.png").convert_alpha()
block = pygame.image.load("img/map/block.png").convert_alpha()
break_block = pygame.image.load("img/map/break_block.png").convert_alpha()
wall = pygame.image.load("img/map/wall.png").convert_alpha()





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
            level_slide = 0
            load_menu = 1

        
        window_surface.blit(text_150a.render("Choisissez votre niveau", True, white), res_pos(60,0))

        k = i = level_select_offset*5
        if i < 0:
            i = 0
        while i <= k+4: #Affiche la selection des niveaux
            if i+1 > len(fichiers):
                break
            cache = (160+i*325-k*325)+level_slide
            window_surface.blit(minimap_list[round(i)], res_pos(cache, 300))
            window_surface.blit(text_40a.render(fichiers[round(i)], True, white), res_pos(cache, 610))
            if collision_rect(cache, 300, 265, 400)[1] == True: #Si un niveau est activé
                window_surface.fill(black)
                window_surface.blit(text_150a.render("Chargement...", True, white), res_pos(450,425))
                pygame.display.flip()
                result = md.load(fichiers[i], res, pygame, Image, ground, block, break_block, wall) #Chargement du niveau selectionné
                if result == "Invalid extension" or result == "Corrupted map":
                    menu = 10
                else:
                    menu = 3
            i += 1
        
        if level_select_offset*5 < len(fichiers)-5:
            if collision_rect_texture(1800, 360, right_arrow, right_arrow_rect) == True:
                level_select_offset += 1
                level_slide = 200
                mouse_click_left = False
        if level_select_offset*5 >= 4:
            if collision_rect_texture(25, 360, left_arrow, left_arrow_rect) == True:
                level_select_offset -= 1
                level_slide = -200
                mouse_click_left = False

        if level_slide < 0:
            level_slide += 50
        elif level_slide > 0:
            level_slide -= 50

        if menu == 1:
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
            collisions = md.collisions_updater([])
            load_menu = 3
        collisition_modification = []

        
        collisions = md.collisions_updater([collisition_modification])
        md.displayer(window_surface, warn)
        

        if bb == True:     # Normalement il suffit de prendre ca pour poser des bombes, mais c'est cursed (je crois)       
            if bbomb.explosion(dt) > 0:
                bbomb.poseBomb(player1, window_surface)
            else:
                bb = False        
        
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
            window_surface.blit(s, (0,0))    # (0,0) are the top-left coordinates
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
