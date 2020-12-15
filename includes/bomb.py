import pygame
pygame.mixer.init()

class Bomb(): # Création de la casse de la bombe
    
    def __init__(self, sprite, posx, posy, power, explo1, explo2, explo3, explo4, explo5, explo_sound, boom, tt):
        self.original_sprite = pygame.image.load(sprite)
        self.x = posx
        self.y = posy
        self.power = power
        self.timer = 190
        self.original_explosion_list = [pygame.image.load(explo1), pygame.image.load(explo2), pygame.image.load(explo3), pygame.image.load(explo4), pygame.image.load(explo5)]
        self.original_ttimg = pygame.image.load(tt)
        self.blockscale = 0
        self.maplimit = [0,0]
        self.centeringmap = [0, 0] 
        self.explo_sound = pygame.mixer.Sound(explo_sound)
        self.boom = pygame.mixer.Sound(boom)

    def bomb_init(self, blockscale, centeringmapx, centeringmapy, maplimit):
        self.blockscale = blockscale
        self.sprite = pygame.transform.scale(self.original_sprite, (blockscale, blockscale))
        self.explosion_list = [pygame.transform.scale(self.original_explosion_list[0], (blockscale, blockscale)),
                                pygame.transform.scale(self.original_explosion_list[1], (blockscale, blockscale)),
                                pygame.transform.scale(self.original_explosion_list[2], (blockscale, blockscale)),
                                pygame.transform.scale(self.original_explosion_list[3], (blockscale, blockscale)),
                                pygame.transform.scale(self.original_explosion_list[4], (blockscale, blockscale))]
        self.ttimg = pygame.transform.smoothscale(self.original_ttimg, (blockscale, blockscale))
        self.maplimit = [maplimit[0],maplimit[1]]
        self.centeringmap = [centeringmapx, centeringmapy] 

    def poseBomb(self, surface, bomb_index, explosion_index, frame_compensation, collisions_update, pause, oenable):
        bomb_index_temp = []
        if pause == False:    
            if bomb_index != []:
                for i in range(len(bomb_index)):   
                    surface.blit(self.sprite, [bomb_index[i][0], bomb_index[i][1]])
                    bomb_index[i][2] -= 1*frame_compensation
                    if bomb_index[i][2] > 0:
                        bomb_index_temp.append(bomb_index[i])
                    else:
                        explosion_index.append([bomb_index[i][0], bomb_index[i][1], 4, [self.power,0]])
                        collisions_update.append([(int((self.maplimit[0]+1)*((bomb_index[i][1]-self.centeringmap[1])/self.blockscale)+((bomb_index[i][0]-self.centeringmap[0])/self.blockscale))), 0])
                        if oenable == False: #dans cette pour placer le random prout (n'oublie pas d'import le sfx dans __init__!)
                            self.explo_sound.play()
                        else:
                            self.boom.play()
        else:
            for i in range(len(bomb_index)):   
                surface.blit(self.sprite, [bomb_index[i][0], bomb_index[i][1]])
            bomb_index_temp = bomb_index

        return bomb_index_temp, explosion_index, collisions_update


    def explosion(self, window_surface, explosion_data, collisions, collisions_update, pause, bomb_data, oenable):
        temp_list_explosion_data = []
        remove_bomb = []
        bomb_data_temp = []
        if pause == False:
            if explosion_data != []:
                for i in range(len(explosion_data)):
                    
                    collisions_update.append([(int((self.maplimit[0]+1)*((explosion_data[i][1]-self.centeringmap[1])/self.blockscale)+((explosion_data[i][0]-self.centeringmap[0])/self.blockscale))), 4])
                
                    if explosion_data[i][3][0] > 0 and explosion_data[i][2] == 4:
                        #gauche
                        if explosion_data[i][3][1] == 0 and collisions[(int((self.maplimit[0]+1)*((explosion_data[i][1]-self.centeringmap[1])/self.blockscale)+(((explosion_data[i][0]-self.blockscale)-self.centeringmap[0])/self.blockscale)))] != 1 or explosion_data[i][3][1] == 1 and collisions[(int((self.maplimit[0]+1)*((explosion_data[i][1]-self.centeringmap[1])/self.blockscale)+(((explosion_data[i][0]-self.blockscale)-self.centeringmap[0])/self.blockscale)))] != 1:
                            if collisions[(int((self.maplimit[0]+1)*((explosion_data[i][1]-self.centeringmap[1])/self.blockscale)+(((explosion_data[i][0]-self.blockscale)-self.centeringmap[0])/self.blockscale)))] == 0:
                                temp_list_explosion_data.append([explosion_data[i][0]-self.blockscale, explosion_data[i][1], 4, [explosion_data[i][3][0]-1,1]])
                            elif collisions[(int((self.maplimit[0]+1)*((explosion_data[i][1]-self.centeringmap[1])/self.blockscale)+(((explosion_data[i][0]-self.blockscale)-self.centeringmap[0])/self.blockscale)))] == 3:
                                temp_list_explosion_data.append([explosion_data[i][0]-self.blockscale, explosion_data[i][1], 4, [self.power,0]])
                                collisions_update.append([(int((self.maplimit[0]+1)*((explosion_data[i][1]-self.centeringmap[1])/self.blockscale)+(((explosion_data[i][0]-self.blockscale)-self.centeringmap[0])/self.blockscale))), 4])
                                for a in range(len(bomb_data)):
                                    if bomb_data[a] == [explosion_data[i][0]-self.blockscale, explosion_data[i][1], bomb_data[a][2]]:
                                        remove_bomb.append(bomb_data[a])
                            else:
                                temp_list_explosion_data.append([explosion_data[i][0]-self.blockscale, explosion_data[i][1], 4, [0,1]])
                                collisions_update.append([(int((self.maplimit[0]+1)*((explosion_data[i][1]-self.centeringmap[1])/self.blockscale)+(((explosion_data[i][0]-self.blockscale)-self.centeringmap[0])/self.blockscale))), 0])
                        
                        #haut    
                        if explosion_data[i][3][1] == 0 and collisions[(int((self.maplimit[0]+1)*(((explosion_data[i][1]-self.blockscale)-self.centeringmap[1])/self.blockscale)+((explosion_data[i][0]-self.centeringmap[0])/self.blockscale)))] != 1 or explosion_data[i][3][1] == 2 and collisions[(int((self.maplimit[0]+1)*(((explosion_data[i][1]-self.blockscale)-self.centeringmap[1])/self.blockscale)+((explosion_data[i][0]-self.centeringmap[0])/self.blockscale)))] != 1:    
                            if collisions[(int((self.maplimit[0]+1)*(((explosion_data[i][1]-self.blockscale)-self.centeringmap[1])/self.blockscale)+((explosion_data[i][0]-self.centeringmap[0])/self.blockscale)))] == 0:
                                temp_list_explosion_data.append([explosion_data[i][0], explosion_data[i][1]-self.blockscale, 4, [explosion_data[i][3][0]-1,2]])
                            elif collisions[(int((self.maplimit[0]+1)*(((explosion_data[i][1]-self.blockscale)-self.centeringmap[1])/self.blockscale)+((explosion_data[i][0]-self.centeringmap[0])/self.blockscale)))] == 3:
                                temp_list_explosion_data.append([explosion_data[i][0], explosion_data[i][1]-self.blockscale, 4, [self.power,0]])
                                collisions_update.append([(int((self.maplimit[0]+1)*(((explosion_data[i][1]-self.blockscale)-self.centeringmap[1])/self.blockscale)+((explosion_data[i][0]-self.centeringmap[0])/self.blockscale))), 4])
                                for a in range(len(bomb_data)):
                                    if bomb_data[a] == [explosion_data[i][0], explosion_data[i][1]-self.blockscale, bomb_data[a][2]]:
                                        remove_bomb.append(bomb_data[a])
                            else:
                                temp_list_explosion_data.append([explosion_data[i][0], explosion_data[i][1]-self.blockscale, 4, [0,2]])
                                collisions_update.append([(int((self.maplimit[0]+1)*(((explosion_data[i][1]-self.blockscale)-self.centeringmap[1])/self.blockscale)+((explosion_data[i][0]-self.centeringmap[0])/self.blockscale))), 0])
                        
                        #droite
                        if explosion_data[i][3][1] == 0 and collisions[(int((self.maplimit[0]+1)*((explosion_data[i][1]-self.centeringmap[1])/self.blockscale)+(((explosion_data[i][0]+self.blockscale)-self.centeringmap[0])/self.blockscale)))] != 1 or explosion_data[i][3][1] == 3 and collisions[(int((self.maplimit[0]+1)*((explosion_data[i][1]-self.centeringmap[1])/self.blockscale)+(((explosion_data[i][0]+self.blockscale)-self.centeringmap[0])/self.blockscale)))] != 1:
                            if collisions[(int((self.maplimit[0]+1)*((explosion_data[i][1]-self.centeringmap[1])/self.blockscale)+(((explosion_data[i][0]+self.blockscale)-self.centeringmap[0])/self.blockscale)))] == 0:
                                temp_list_explosion_data.append([explosion_data[i][0]+self.blockscale, explosion_data[i][1], 4, [explosion_data[i][3][0]-1,3]])
                            elif collisions[(int((self.maplimit[0]+1)*((explosion_data[i][1]-self.centeringmap[1])/self.blockscale)+(((explosion_data[i][0]+self.blockscale)-self.centeringmap[0])/self.blockscale)))] == 3:
                                temp_list_explosion_data.append([explosion_data[i][0]+self.blockscale, explosion_data[i][1], 4, [self.power,0]])
                                collisions_update.append([(int((self.maplimit[0]+1)*((explosion_data[i][1]-self.centeringmap[1])/self.blockscale)+(((explosion_data[i][0]+self.blockscale)-self.centeringmap[0])/self.blockscale))), 4])
                                for a in range(len(bomb_data)):
                                    if bomb_data[a] == [explosion_data[i][0]+self.blockscale, explosion_data[i][1], bomb_data[a][2]]:
                                        remove_bomb.append(bomb_data[a])
                            else:
                                temp_list_explosion_data.append([explosion_data[i][0]+self.blockscale, explosion_data[i][1], 4, [0,3]])
                                collisions_update.append([(int((self.maplimit[0]+1)*((explosion_data[i][1]-self.centeringmap[1])/self.blockscale)+(((explosion_data[i][0]+self.blockscale)-self.centeringmap[0])/self.blockscale))), 0])
                        
                        #bas
                        if explosion_data[i][3][1] == 0 and collisions[(int((self.maplimit[0]+1)*(((explosion_data[i][1]+self.blockscale)-self.centeringmap[1])/self.blockscale)+((explosion_data[i][0]-self.centeringmap[0])/self.blockscale)))] != 1 or explosion_data[i][3][1] == 4 and collisions[(int((self.maplimit[0]+1)*(((explosion_data[i][1]+self.blockscale)-self.centeringmap[1])/self.blockscale)+((explosion_data[i][0]-self.centeringmap[0])/self.blockscale)))] != 1:
                            if collisions[(int((self.maplimit[0]+1)*(((explosion_data[i][1]+self.blockscale)-self.centeringmap[1])/self.blockscale)+((explosion_data[i][0]-self.centeringmap[0])/self.blockscale)))] == 0:
                                temp_list_explosion_data.append([explosion_data[i][0], explosion_data[i][1]+self.blockscale, 4, [explosion_data[i][3][0]-1,4]])
                            if collisions[(int((self.maplimit[0]+1)*(((explosion_data[i][1]+self.blockscale)-self.centeringmap[1])/self.blockscale)+((explosion_data[i][0]-self.centeringmap[0])/self.blockscale)))] == 3:
                                temp_list_explosion_data.append([explosion_data[i][0], explosion_data[i][1]+self.blockscale, 4, [self.power,0]])
                                collisions_update.append([(int((self.maplimit[0]+1)*(((explosion_data[i][1]+self.blockscale)-self.centeringmap[1])/self.blockscale)+((explosion_data[i][0]-self.centeringmap[0])/self.blockscale))), 4])
                                for a in range(len(bomb_data)):
                                    if bomb_data[a] == [explosion_data[i][0], explosion_data[i][1]+self.blockscale, bomb_data[a][2]]:
                                        remove_bomb.append(bomb_data[a])
                            else:
                                temp_list_explosion_data.append([explosion_data[i][0], explosion_data[i][1]+self.blockscale, 4, [0,4]])
                                collisions_update.append([(int((self.maplimit[0]+1)*(((explosion_data[i][1]+self.blockscale)-self.centeringmap[1])/self.blockscale)+((explosion_data[i][0]-self.centeringmap[0])/self.blockscale))), 0])
                    

                    if oenable == False:
                        window_surface.blit(self.explosion_list[4-explosion_data[i][2]], (explosion_data[i][0], explosion_data[i][1]))
                    else:
                        window_surface.blit(self.ttimg, (explosion_data[i][0], explosion_data[i][1]))

                    if explosion_data[i][2] > 0:
                        explosion_data[i][2] -= 1
                        temp_list_explosion_data.append(explosion_data[i])
                    else:
                        collisions_update.append([(int((self.maplimit[0]+1)*((explosion_data[i][1]-self.centeringmap[1])/self.blockscale)+((explosion_data[i][0]-self.centeringmap[0])/self.blockscale))), 0])
        else:
            temp_list_explosion_data = explosion_data
            for i in range(len(explosion_data)):
                if oenable == False:
                    window_surface.blit(self.explosion_list[4-explosion_data[i][2]], (explosion_data[i][0], explosion_data[i][1]))
                else:
                    window_surface.blit(self.ttimg, (explosion_data[i][0], explosion_data[i][1]))


        if remove_bomb != []:
            for i in range(len(bomb_data)):
                exist = False
                for k in range(len(remove_bomb)):
                    if remove_bomb[k] == bomb_data[i]:
                        exist = True
                if exist == False:
                    bomb_data_temp.append(bomb_data[i])
        else:
            bomb_data_temp = bomb_data

        return temp_list_explosion_data, collisions_update, bomb_data_temp
        