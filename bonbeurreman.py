# -*-coding:Utf-8 -*
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
    input("pip à été mis à jour et pygame a été installé.\nSi le programme ne se lance toujours pas, faite manuellement les installations\nPour installer voici la marche à suivre:\nPremièrement faites 'windows+r', tapez 'cmd' et appuyer sur entré.\n Nous allons d'abbord vérifier que pip est à jour, entrez la commande si dessous dans l'invite de commande que vous avez ouvert:\npython -m pip install --upgrade pip\nAttendez la fin de l'instalation et entrez ensuite cette commande pour installer pygame:\npip install pygame\n Une fois l'installation terminé vous devriez pouvoir lancer correctement ce programme\n Appuyez sur entrée pour continuer.\n\n")
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
    input("pip à été mis à jour et pil a été installé.\nSi le programme ne se lance toujours pas, faite manuellement les installations\nPour installer voici la marche à suivre:\nPremièrement faites 'windows+r', tapez 'cmd' et appuyer sur entré.\n Nous allons d'abbord vérifier que pip est à jour, entrez la commande si dessous dans l'invite de commande que vous avez ouvert:\npython -m pip install --upgrade pip\nAttendez la fin de l'instalation et entrez ensuite cette commande pour installer pil:\npip install pillow\n Une fois l'installation terminé vous devriez pouvoir lancer correctement ce programme\n Appuyez sur entrée pour continuer.\n\n")
    from PIL import Image

import includes.player as player
import includes.bomb as bomb
import includes.mapdisplayer as mapdisplayer
import includes.keyboard_input_detect as keyboard_input_detect
import includes.map_file_load_indexer as map_indexer
import includes.mapeditor as mapeditor
import ctypes
from os import listdir, remove
from os.path import dirname, realpath
from pickle import Unpickler
from random import randint




print("Jeu réalisé par Tony, Jean-Pierre, Kimi et Lenny")
print("Démarage de BonBeurreMan...")
script_path = dirname(realpath(__file__))
script_path = script_path.replace("\\", "/")
# Definitions des variables -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
player1 = player.Player(f"{script_path}/img/player_stuff/BlueBirdyBomber.png", f"{script_path}/BomberMan ST/set_bomb.ogg", f"{script_path}/img/hidden/tt.ogg", f"{script_path}/BomberMan ST/PowerUpSound.ogg")
player2 = player.Player(f"{script_path}/img/player_stuff/RedBirdyBomber.png", f"{script_path}/BomberMan ST/set_bomb.ogg", f"{script_path}/img/hidden/tt.ogg", f"{script_path}/BomberMan ST/PowerUpSound.ogg")
bbomb = bomb.Bomb(f"{script_path}/img/bomb/bomb_pixel.png", player1.x, player1.y, 2, f"{script_path}/img/bomb/explosion/explo1.png", f"{script_path}/img/bomb/explosion/explo2.png", f"{script_path}/img/bomb/explosion/explo3.png", f"{script_path}/img/bomb/explosion/explo4.png", f"{script_path}/img/bomb/explosion/explo5.png",  f"{script_path}/BomberMan ST/Explosion_SFX.ogg", f"{script_path}/img/hidden/boom.ogg", f"{script_path}/img/hidden/tt.png")

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
butter = (253,219,148)

res = [1280, 720] # Definition de la résolution d'affichage
# res = [640, 360]
mx = 0 # Definition de la position x de la souris
my = 0 # Definition de la position y de la souris
mousepress = [0,0,0] # Permet d'acceder au input de la souris, sachant que mousepress[0] = click gauche, mousepress[1] = click molette, mousepress[2] = click droit
devmode = False
menu = 0 #Menu d'entrée
load_menu = 0 #Variable permettant de charger a la première frame du menu actif

mouse_click_left = True # Variable a utiliser si l'on veut que l'utilisateur relache le click

fichiers = map_indexer.map_file_indexer(script_path, listdir, Image, Unpickler, remove)
editor = mapeditor.MapEditor(res)
minimap_list = []


result = "ok"
level_select_offset = 0
pause = False
escape_released = True
bb = False
level_slide = 0
arrows = (False, False)
arrows_slide = [0,0]
fade_var = [0, 0]
temp_menu = 0
fullscreen = False
o = 0
oenable = False
    
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
    touched = False                                                                     # (mettre la variable mouse_click_left)(par défaut actif))
    window_surface.blit(texture, res_pos(x,y))
    if texture_rect.collidepoint(mx,my) == 1:
        touched = True 
        if mousepress[0] and mouse_click_left == True or mousepress[0] and click_block_condition == True:
            pressed = True
    return (touched, pressed)

def fade_in(fade, fmenu, ftemp_menu, initial_menu):
    if oenable == False:    
        if fade == [255, -1]:
            fmenu = ftemp_menu
            window_surface.fill(black)
        if fade == [0, 1]:
            ftemp_menu = fmenu
            fmenu = initial_menu
        if fade[1] == 1:
            if fade[0] + 20 < 255:
                s.set_alpha(fade[0] + 20*frame_compensation)
                fade[0] += 20*frame_compensation
            else:   
                s.set_alpha(255)
                fade = [255, -1]
        if fade[1] == -1 and fade[0] != 0 and fmenu == ftemp_menu:
            if fade[0] - 20 > 0:
                s.set_alpha(fade[0] - 20*frame_compensation)
                fade[0] -= 20*frame_compensation  
            else:
                s.set_alpha(0)
                fade = [0, 0]
    else:
        if fade == [0, 1]:
            ftemp_menu = fmenu
            fmenu = initial_menu
            hisong.set_volume(0.4)
            hisong.play()
            fade[0] += 1
        if fade[0] > 0 and fade[0] < 8:
            fade[0] += 1
            window_surface.blit(hiimg, res_pos(400,90))
        if fade[0] > 7 and fade[0] < 16:
            fade[0] += 1
            window_surface.blit(hiimg, res_pos(400,135))
        if fade[0] > 15 and fade[0] < 23:
            fade[0] += 1
            window_surface.blit(hiimg, res_pos(400,45))
        if fade[0] > 22 and fade[0] < 30:
            fade[0] += 1
            window_surface.blit(hiimg, res_pos(400,90))
            if fade[0] > 29:
                fmenu = ftemp_menu
                fade = [0,0]
    return (fade, fmenu, ftemp_menu)


pygame.init() # Lancement de pygame -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

clock = pygame.time.Clock()

pygame.display.set_caption("BonBeurreMan") # Renommer l'intitulé de la fenêtre

ctypes.windll.user32.SetProcessDPIAware()
window_surface = pygame.display.set_mode(res)
md = mapdisplayer.Mapdislayer(res, script_path, pygame)


#Chargement des polices d'écritures
fps_text = pygame.font.Font(f"{script_path}/fonts/VCR_OSD_MONO_1.ttf", round(res_adaptation(33))) # Autres
text_40a = pygame.font.Font(f"{script_path}/fonts/arialbd.ttf", round(res_adaptation(60)))
text_150a = pygame.font.Font(f"{script_path}/fonts/arialbd.ttf", round(res_adaptation(150)))
butter_font = pygame.font.Font(f"{script_path}/fonts/creamy butter.ttf", round(res_adaptation(120)))

window_surface.blit(text_150a.render("Chargement...", True, butter), res_pos(450,425))
pygame.display.flip()

#Chargement sons

# main_sound = pygame.mixer.Sound(f"{script_path}/BomberMan ST/soundtrackbomberman.wav")
osong = pygame.mixer.Sound(f"{script_path}/img/hidden/o.ogg")
csong = pygame.mixer.Sound(f"{script_path}/img/hidden/c.ogg")
oesong = pygame.mixer.Sound(f"{script_path}/img/hidden/oe.ogg")
hisong = pygame.mixer.Sound(f"{script_path}/img/hidden/hi.ogg")

#Chargement des textures

s = pygame.Surface(res)  # the size of your rect
s.set_alpha(0)           # alpha level
s.fill((0, 0, 0))        # this fills the entire surface

a = pygame.Surface(res)
a.set_alpha(128)         
a.fill((0, 0, 0))      

for i in range(len(fichiers)):
    minimapimg = pygame.image.load(f"{script_path}/img/temp/mini_map/{fichiers[i]}_cache.png").convert_alpha()
    minimapimg = pygame.transform.smoothscale(minimapimg, res_pos(265,265))
    minimap_list.append(minimapimg)

oimg = pygame.image.load(f"{script_path}/img/hidden/o.png").convert_alpha()
oimg = pygame.transform.smoothscale(oimg, res_pos(1218, 900))
hiimg = pygame.image.load(f"{script_path}/img/hidden/hi.png").convert_alpha()
hiimg = pygame.transform.smoothscale(hiimg, res_pos(1218, 900))

warn = pygame.image.load(f"{script_path}/img/ui/warn.png").convert_alpha() #Fonction pour importer l'image
warn = pygame.transform.smoothscale(warn, res_pos(220,200)) #N'utiliser pas smooth scale sur un pixel art car ca le rendrait flou
# warn = pygame.transform.scale(warn, res_pos(220,200)) #Fonction pour la scale a la résolution d'affichage

left_arrow = pygame.image.load(f"{script_path}/img/ui/left_arrow.png").convert_alpha()
left_arrow = pygame.transform.smoothscale(left_arrow, res_pos(95,180))

right_arrow = pygame.image.load(f"{script_path}/img/ui/right_arrow.png").convert_alpha()
right_arrow = pygame.transform.smoothscale(right_arrow, res_pos(95,180))

beurre = pygame.image.load(f"{script_path}/img/ui/beurre.png").convert_alpha()
beurre = pygame.transform.smoothscale(beurre, res_pos(400,267))
logo = pygame.image.load(f"{script_path}/img/ui/logo.png").convert_alpha()
logo = pygame.transform.smoothscale(logo, res_pos(500,300))
bg = pygame.image.load(f"{script_path}/img/ui/horrible.png").convert_alpha()
bg = pygame.transform.smoothscale(bg, res_pos(1920, 1080))
beurre2 = pygame.transform.smoothscale(beurre, res_pos(1920, 1080))
ground = pygame.image.load(f"{script_path}/img/map/ground.png").convert_alpha()
# block = pygame.image.load(f"{script_path}/img/map/block.png").convert_alpha()
# wall = pygame.image.load(f"{script_path}/img/map/wall.png").convert_alpha()
# joueur_sprite = pygame.image.load(f"{script_path}/img/player_stuff/perso.png").convert_alpha()





# main_sound.play()

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
            temp_menu = 0
            load_menu = 0
            o = 0
        
        window_surface.blit(bg,(0,0))
        window_surface.blit(butter_font.render("BonBeurreMan", True, butter), res_pos(330,0))

        if collision_rect(810, 300, 300, 150,"Jouer")[1] == True and temp_menu == 0: #Passe sur le menu de selection de niveau
            menu = 1
            fade_var = [0, 1]
            level_select_offset = 0

        if collision_rect(810, 500, 300, 150, "Options")[1] == True and temp_menu == 0: #Passe sur les options
            menu = 2
            fade_var = [0, 1]
        if collision_rect(810, 700, 300, 150, "Editeur de cartes")[1] == True and temp_menu == 0: #Passe sur éditeur de cartes
            # menu = 4
            # fade_var = [0, 1]
            pass
        if collision_rect(810, 900, 300, 150, "Quitter")[1] == True and temp_menu == 0: #Ferme le jeu
            launched = False
        
        window_surface.blit(beurre, res_pos(1450, 780))
        window_surface.blit(logo,res_pos(0,800))

        if keyboard_input["o"] == True or o > 0: #Un easter egg à la con faites pas gaffe
            if o == 0:
                o = 1
                print("o")
            if keyboard_input["b"] == True or o > 1:
                if o == 1:
                    o = 2
                    print("ob")
                if keyboard_input["j"] == True or o > 2:
                    if o == 2:
                        o = 3
                        print("obj")
                    if keyboard_input["e"] == True or o > 3:
                        if o == 3:
                            o = 4
                            print("obje")
                        if keyboard_input["c"] == True or o > 4:
                            if o == 4:
                                o = 5
                                print("objec")
                            if keyboard_input["t"] == True or o > 5:
                                if o == 5:
                                    o = 6
                                    print("object")
                                if keyboard_input["i"] == True or o > 6:
                                    if o == 6:
                                        o = 7
                                        print("objecti")
                                    if keyboard_input["o"] == True or o > 7:
                                        if o == 7:
                                            o = 8
                                            print("objectio")
                                        if keyboard_input["n"] == True or o > 8:
                                            if o == 8:
                                                o = 9
                                                
                                                print("objection!")
                                                if oenable == False:
                                                    osong.play()
                                                    oenable = True
                                                else:
                                                    oesong.play()
                                                    csong.stop()
                                                    oenable = False
                                            
                                            if o > 8 and o < 15:
                                                o += 1
                                                window_surface.blit(oimg, res_pos(400,90))
                                            elif o > 14 and o < 22:
                                                o += 1
                                                window_surface.blit(oimg, res_pos(400,135))
                                            elif o > 21 and o < 28:
                                                o += 1
                                                window_surface.blit(oimg, res_pos(400,45))
                                            elif o > 27 and o < 35:
                                                o += 1
                                                window_surface.blit(oimg, res_pos(400,90))
                                            else:
                                                o = 0
                                                if oenable == True:
                                                    csong.set_volume(0.5)
                                                    csong.play(-1)

    
        fade_var, menu, temp_menu = fade_in(fade_var, menu, temp_menu, 0)

    if menu == 1: #Selection du niveau --------------------------------------------------------------------------------------------------------------------------------------------------------
        if load_menu != 1: # Mettez ici les éléments a charger une seule fois
            mouse_click_left = False
            left_arrow_rect = left_arrow.get_rect(topleft=res_pos(25,350))
            right_arrow_rect = right_arrow.get_rect(topleft=res_pos(1800,350))
            level_slide = 0
            arrows = (False, False)
            arrows_slide = [0,0]
            arrows_slide_move = 15
            pause = False
            load_menu = 1
        
        window_surface.blit(beurre2, res_pos(0,0))
        window_surface.blit(text_150a.render("Choisissez votre niveau", True, butter), res_pos(100,0))

        k = i = level_select_offset*5
        if i < 0:
            i = 0
        while i <= k+4: #Affiche la selection des niveaux
            if i+1 > len(fichiers):
                break
            cache = (160+i*325-k*325)+level_slide
            window_surface.blit(minimap_list[round(i)], res_pos(cache, 300))
            window_surface.blit(text_40a.render(fichiers[round(i)], True, black), res_pos(cache+3, 613))
            window_surface.blit(text_40a.render(fichiers[round(i)], True, white), res_pos(cache, 610))
            if collision_rect(cache, 300, 265, 400)[1] == True: #Si un niveau est activé
                fade_var = [0, 0]
                window_surface.fill(black)
                window_surface.blit(text_150a.render("Chargement...", True, white), res_pos(450,425))
                pygame.display.flip()
                result = md.load(fichiers[i], res, pygame, Image, script_path, Unpickler, randint) #Chargement du niveau selectionné
                if result == "Invalid extension" or result == "Corrupted map":
                    menu = 10
                else:
                    menu = 3
            i += 1
        
        if level_select_offset*5 < len(fichiers)-5:
            arrows = collision_rect_texture(1800+arrows_slide[1], 360, right_arrow, right_arrow_rect) #Fleche droite
            if arrows[1] == True:
                level_select_offset += 1
                level_slide = 200
                mouse_click_left = False
                arrows_slide = [arrows_slide[0], 0]
            elif arrows[0] == True and arrows_slide[1] < 25:
                arrows_slide = [arrows_slide[0], arrows_slide[1]+arrows_slide_move]
            elif arrows[0] == False:
                arrows_slide = [arrows_slide[0], 0]
            else:
                arrows_slide = [arrows_slide[0], 25]
        if level_select_offset*5 >= 4:
            arrows = collision_rect_texture(25-arrows_slide[0], 360, left_arrow, left_arrow_rect) #Fleche gauche
            if arrows[1] == True:
                level_select_offset -= 1
                level_slide = -200
                mouse_click_left = False
                arrows_slide = [0, arrows_slide[1]]
            elif arrows[0] == True and arrows_slide[0] < 25:
                arrows_slide = [arrows_slide[0]+arrows_slide_move, arrows_slide[1]]
            elif arrows[0] == False:
                arrows_slide = [0, arrows_slide[1]]
            else:
                arrows_slide = [25, arrows_slide[1]]


        if level_slide < 0:
            level_slide += 50
        elif level_slide > 0:
            level_slide -= 50

        if menu == 1:
            if collision_rect(0, 975, 300, 105, "Retour")[1] == True:
                menu = 0
                fade_var = [0, 1]
            # if collision_rect(1320, 975, 600, 105, "Connecter manettes")[1] == True:
            #     pass
            # if collision_rect(490, 975, 675, 105, "Connexion multi local")[1] == True:
            #     pass
        
        fade_var, menu, temp_menu = fade_in(fade_var, menu, temp_menu, 1)
            


    
    if menu == 2: #Options --------------------------------------------------------------------------------------------------------------------------------------------------------
        if load_menu != 2: # Mettez ici les éléments a charger une seule fois
            mouse_click_left = False
            load_menu = 2
        
        if collision_rect(0, 975, 300, 105, "Retour")[1] == True:
            menu = 0
            fade_var = [0, 1]

        if collision_rect(200, 200, 300, 105, "Plein écran")[1] == True:
            if fullscreen == False:
                if res[1] == 1080:
                    ctypes.windll.user32.SetProcessDPIAware()
                window_surface = pygame.display.set_mode(res, pygame.FULLSCREEN)
                fullscreen = True
            else:
                window_surface = pygame.display.set_mode(res)
                fullscreen = False 

        

        fade_var, menu, temp_menu = fade_in(fade_var, menu, temp_menu, 2)
            
    
    if menu == 3: #Jeu -----------------------------------------------------------------------------------------------------------------------------------------------------------------
        if load_menu != 3: # Mettez ici les éléments a charger une seule fois
            mouse_click_left = False
            collisions = md.collisions_updater([])
            player_numb = 2
            player1.player_start(md.blockscale, md.playersspawns[0], md.centeringmapx, md.centeringmapy, md.maplimit, 1)
            player2.player_start(md.blockscale, md.playersspawns[1], md.centeringmapx, md.centeringmapy, md.maplimit, 2)
            bbomb.bomb_init(md.blockscale, md.centeringmapx, md.centeringmapy, md.maplimit)
            end_game = []
            player1.max_bomb, player1.power, player1.lag_temp = 1, 2, 6
            player2.max_bomb, player2.power, player2.lag_temp= 1, 2, 6

            for i in range(player_numb):
                end_game.append(True)
            release_space = True
            lag = 0
            bomb_data = []
            explosion_data = []
            release_rshift = True
            load_menu = 3
            
        collisition_modification = []
 
        if pause == False:
            player1.movement(keyboard_input, collisions, frame_compensation)  
            player2.movementp2(keyboard_input, collisions, frame_compensation)

            if len(player1.bomb_list) > 0: # gérance des timer des bombes a l'interieur de la liste
                n = 0
                for i in player1.bomb_list:
                    player1.bomb_list[n] -= 1
                    n += 1

            if len(player2.bomb_list) > 0: # gérance des timer des bombes a l'interieur de la liste
                m = 0
                for i in player2.bomb_list:
                    player2.bomb_list[m] -= 1
                    m += 1

            if keyboard_input["SPACE"] == True and release_space == True:
                # print(player1.bomb_list)
                bbomb.power = player1.power
                bomb_data, collisition_modification = player1.set_bomb(collisition_modification, oenable, bomb_data)

            if keyboard_input["RSHIFT"] == True and release_space == True:
                # print(player2.bomb_list)
                bbomb.power = player2.power
                bomb_data, collisition_modification = player2.set_bomb(collisition_modification, oenable, bomb_data)


            player1.bonus_checker(md.powerup_data)  #fonctions qui va check les bonus au sol
            player2.bonus_checker(md.powerup_data)  #fonctions qui va check les bonus au sol
        
        md.displayer(window_surface)
        
        bomb_data, explosion_data, collisition_modification = bbomb.poseBomb(window_surface, bomb_data, explosion_data, frame_compensation, collisition_modification, pause, oenable)
        explosion_data, collisition_modification, bomb_data = bbomb.explosion(window_surface, explosion_data, collisions, collisition_modification, pause, bomb_data, oenable)
        player1.player_display(window_surface, frame_compensation, end_game[0])
        player2.player_display(window_surface, frame_compensation, end_game[1])
        
        
        collisions = md.collisions_updater(collisition_modification)

        end_game = player1.kill(collisions, end_game)
        end_game = player2.kill(collisions, end_game)
        
        

        player_left = 0
        for i in range(player_numb):
            if end_game[i] == True:
                player_left += 1
        
        if player_left <= 1:
            pause = True
            window_surface.blit(a, (0,0))    # (0,0) are the top-left coordinates
            window_surface.blit(text_150a.render("Fin de partie", True, white), res_pos(510,0))
            for i in range(player_numb):
                if end_game[i] == True:
                    window_surface.blit(text_150a.render(f"Joueur {i+1} a gagné", True, white), res_pos(340,200))
            if collision_rect(530, 700, 825, 105, "Retour au choix des niveaux")[1] == True:
                menu = 1
                fade_var = [0, 1]

        else:
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

            if keyboard_input["SPACE"] == True:
                release_space = False
            else:
                release_space = True

            if keyboard_input["RSHIFT"] == True:
                release_rshift = False
            else:
                release_rshift = True

            if pause == True:
                window_surface.blit(a, (0,0))    # (0,0) are the top-left coordinates
                window_surface.blit(text_150a.render("Pause", True, white), res_pos(720,0))
                if collision_rect(790, 500, 300, 105, "Continuer")[1] == True:
                    pause = False
                if collision_rect(530, 700, 825, 105, "Retour au choix des niveaux")[1] == True:
                    menu = 1
                    fade_var = [0, 1]
        
        fade_var, menu, temp_menu = fade_in(fade_var, menu, temp_menu, 3)

    if menu == 4: #Selection
        if load_menu != 4: # Mettez ici les éléments a charger une seule fois
            mouse_click_left = False
            left_arrow_rect = left_arrow.get_rect(topleft=res_pos(25,350))
            right_arrow_rect = right_arrow.get_rect(topleft=res_pos(1800,350))
            level_slide = 0
            arrows = (False, False)
            arrows_slide = [0,0]
            arrows_slide_move = 15
            pause = False
            load_menu = 4

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
                fade_var = [0, 0]
                window_surface.fill(black)
                window_surface.blit(text_150a.render("Chargement...", True, white), res_pos(450,425))
                pygame.display.flip()
                result = editor.load(fichiers[i], res, pygame, script_path, Unpickler, ground, block, break_block, wall) #Chargement du niveau selectionné
                if result == "Invalid extension" or result == "Corrupted map":
                    menu = 10
                else:
                    menu = 5
            i += 1

        if level_select_offset*5 < len(fichiers)-5:
            arrows = collision_rect_texture(1800+arrows_slide[1], 360, right_arrow, right_arrow_rect) #Fleche droite
            if arrows[1] == True:
                level_select_offset += 1
                level_slide = 200
                mouse_click_left = False
                arrows_slide = [arrows_slide[0], 0]
            elif arrows[0] == True and arrows_slide[1] < 25:
                arrows_slide = [arrows_slide[0], arrows_slide[1]+arrows_slide_move]
            elif arrows[0] == False:
                arrows_slide = [arrows_slide[0], 0]
            else:
                arrows_slide = [arrows_slide[0], 25]
        if level_select_offset*5 >= 4:
            arrows = collision_rect_texture(25-arrows_slide[0], 360, left_arrow, left_arrow_rect) #Fleche gauche
            if arrows[1] == True:
                level_select_offset -= 1
                level_slide = -200
                mouse_click_left = False
                arrows_slide = [0, arrows_slide[1]]
            elif arrows[0] == True and arrows_slide[0] < 25:
                arrows_slide = [arrows_slide[0]+arrows_slide_move, arrows_slide[1]]
            elif arrows[0] == False:
                arrows_slide = [0, arrows_slide[1]]
            else:
                arrows_slide = [25, arrows_slide[1]]


        if level_slide < 0:
            level_slide += 50
        elif level_slide > 0:
            level_slide -= 50

        if collision_rect(0, 975, 300, 105, "Retour")[1] == True:
            menu = 0
            fade_var = [0, 1]
        if collision_rect(1520, 975, 400, 105, "Nouveau")[1] == True:
            menu = 5
            fade_var = [0, 1]

        fade_var, menu, temp_menu = fade_in(fade_var, menu, temp_menu, 4)

    if menu == 5: #Editeur de carte spécialement pour kimi <3
        if load_menu != 5: # Mettez ici les éléments a charger une seule fois
            mouse_click_left = False
            load_menu = 5

        editor.displayer(window_surface)

        fade_var, menu, temp_menu = fade_in(fade_var, menu, temp_menu, 5)           

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
            fade_var = [0, 1]

        fade_var, menu, temp_menu = fade_in(fade_var, menu, temp_menu, 10)
    
    if mousepress[0] == 1:
        mouse_click_left = False
    else:
        mouse_click_left = True

    #Vérifie le click gauche

    if fade_var[0] != 0:
        window_surface.blit(s, (0,0))
    update_fps() # Affiche les fps
    pygame.display.flip() # Met a jour l'affichage
    dt = clock.tick(60)/1000 # Permet de limiter la framerate a 60fps
    frame_compensation = dt/(1/60)
    