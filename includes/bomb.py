import pygame

class Bomb(): # Création de la casse de la bombe
    
    def __init__(self, sprite, posx, posy, explo1, explo2, explo3, explo4, explo5):
        self.sprite = pygame.image.load(sprite)
        self.x = posx
        self.y = posy
        self.timer = 190
        self.explosion_list = [pygame.image.load(explo1), pygame.image.load(explo2), pygame.image.load(explo3), pygame.image.load(explo4), pygame.image.load(explo5)]
        self.blockscale = 0
        self.maplimit = [0,0]
        self.centeringmap = [0, 0] 

    def bomb_init(self, blockscale, centeringmapx, centeringmapy, maplimit):
        self.blockscale = blockscale
        self.sprite = pygame.transform.scale(self.sprite, (blockscale, blockscale))
        self.explosion_list = [pygame.transform.scale(self.explosion_list[0], (blockscale, blockscale)),
                                pygame.transform.scale(self.explosion_list[1], (blockscale, blockscale)),
                                pygame.transform.scale(self.explosion_list[2], (blockscale, blockscale)),
                                pygame.transform.scale(self.explosion_list[3], (blockscale, blockscale)),
                                pygame.transform.scale(self.explosion_list[4], (blockscale, blockscale))]
        self.maplimit = [maplimit[0],maplimit[1]]
        self.centeringmap = [centeringmapx, centeringmapy] 

    def poseBomb(self, surface, bomb_index, explosion_index, frame_compensation):
        bomb_index_temp = []
        collision_update = []
        if bomb_index != []:
            for i in range(len(bomb_index)):   
                surface.blit(self.sprite, [bomb_index[i][0], bomb_index[i][1]])
                bomb_index[i][2] -= 1*frame_compensation
                if bomb_index[i][2] > 0:
                    bomb_index_temp.append(bomb_index[i])
                else:
                    explosion_index.append([bomb_index[i][0], bomb_index[i][1], 4, [2,0]])
                

        return bomb_index_temp, explosion_index#, collision_update


    def explosion(self, window_surface, explosion_data, frame_compensation, collisions):
        temp_list_explosion_data = []
        collisions_update = []
        if explosion_data != []:
            for i in range(len(explosion_data)):
                window_surface.blit(self.explosion_list[4-explosion_data[i][2]], (explosion_data[i][0], explosion_data[i][1]))
                if explosion_data[i][3][0] > 0 and explosion_data[i][2] == 4:
                    if explosion_data[i][3][1] == 0 and collisions[(int((self.maplimit[0]+1)*((explosion_data[i][1]-self.centeringmap[1])/self.blockscale)+(((explosion_data[i][0]-self.blockscale)-self.centeringmap[0])/self.blockscale)))] == 0 or explosion_data[i][3][1] == 1 and collisions[(int((self.maplimit[0]+1)*((explosion_data[i][1]-self.centeringmap[1])/self.blockscale)+(((explosion_data[i][0]-self.blockscale)-self.centeringmap[0])/self.blockscale)))] == 0 or explosion_data[i][3][1] == 0 and collisions[(int((self.maplimit[0]+1)*((explosion_data[i][1]-self.centeringmap[1])/self.blockscale)+(((explosion_data[i][0]-self.blockscale)-self.centeringmap[0])/self.blockscale)))] == 2 or explosion_data[i][3][1] == 1 and collisions[(int((self.maplimit[0]+1)*((explosion_data[i][1]-self.centeringmap[1])/self.blockscale)+(((explosion_data[i][0]-self.blockscale)-self.centeringmap[0])/self.blockscale)))] == 2:
                        if collisions[(int((self.maplimit[0]+1)*((explosion_data[i][1]-self.centeringmap[1])/self.blockscale)+(((explosion_data[i][0]-self.blockscale)-self.centeringmap[0])/self.blockscale)))] == 0:
                            temp_list_explosion_data.append([explosion_data[i][0]-self.blockscale, explosion_data[i][1], 4, [explosion_data[i][3][0]-1,1]])
                        else:
                            temp_list_explosion_data.append([explosion_data[i][0]-self.blockscale, explosion_data[i][1], 4, [0,1]])
                            collisions_update.append([(int((self.maplimit[0]+1)*((explosion_data[i][1]-self.centeringmap[1])/self.blockscale)+(((explosion_data[i][0]-self.blockscale)-self.centeringmap[0])/self.blockscale))), 0])
                    if explosion_data[i][3][1] == 0 and collisions[(int((self.maplimit[0]+1)*(((explosion_data[i][1]-self.blockscale)-self.centeringmap[1])/self.blockscale)+((explosion_data[i][0]-self.centeringmap[0])/self.blockscale)))] == 0 or explosion_data[i][3][1] == 2 and collisions[(int((self.maplimit[0]+1)*(((explosion_data[i][1]-self.blockscale)-self.centeringmap[1])/self.blockscale)+((explosion_data[i][0]-self.centeringmap[0])/self.blockscale)))] == 0 or explosion_data[i][3][1] == 0 and collisions[(int((self.maplimit[0]+1)*(((explosion_data[i][1]-self.blockscale)-self.centeringmap[1])/self.blockscale)+((explosion_data[i][0]-self.centeringmap[0])/self.blockscale)))] == 2 or explosion_data[i][3][1] == 2 and collisions[(int((self.maplimit[0]+1)*(((explosion_data[i][1]-self.blockscale)-self.centeringmap[1])/self.blockscale)+((explosion_data[i][0]-self.centeringmap[0])/self.blockscale)))] == 2:    
                        if collisions[(int((self.maplimit[0]+1)*(((explosion_data[i][1]-self.blockscale)-self.centeringmap[1])/self.blockscale)+((explosion_data[i][0]-self.centeringmap[0])/self.blockscale)))] == 0:
                            temp_list_explosion_data.append([explosion_data[i][0], explosion_data[i][1]-self.blockscale, 4, [explosion_data[i][3][0]-1,2]])
                        else:
                            temp_list_explosion_data.append([explosion_data[i][0], explosion_data[i][1]-self.blockscale, 4, [0,2]])
                            collisions_update.append([(int((self.maplimit[0]+1)*(((explosion_data[i][1]-self.blockscale)-self.centeringmap[1])/self.blockscale)+((explosion_data[i][0]-self.centeringmap[0])/self.blockscale))), 0])
                    if explosion_data[i][3][1] == 0 and collisions[(int((self.maplimit[0]+1)*((explosion_data[i][1]-self.centeringmap[1])/self.blockscale)+(((explosion_data[i][0]+self.blockscale)-self.centeringmap[0])/self.blockscale)))] == 0 or explosion_data[i][3][1] == 3 and collisions[(int((self.maplimit[0]+1)*((explosion_data[i][1]-self.centeringmap[1])/self.blockscale)+(((explosion_data[i][0]+self.blockscale)-self.centeringmap[0])/self.blockscale)))] == 0 or explosion_data[i][3][1] == 0 and collisions[(int((self.maplimit[0]+1)*((explosion_data[i][1]-self.centeringmap[1])/self.blockscale)+(((explosion_data[i][0]+self.blockscale)-self.centeringmap[0])/self.blockscale)))] == 2 or explosion_data[i][3][1] == 3 and collisions[(int((self.maplimit[0]+1)*((explosion_data[i][1]-self.centeringmap[1])/self.blockscale)+(((explosion_data[i][0]+self.blockscale)-self.centeringmap[0])/self.blockscale)))] == 2:
                        if collisions[(int((self.maplimit[0]+1)*((explosion_data[i][1]-self.centeringmap[1])/self.blockscale)+(((explosion_data[i][0]+self.blockscale)-self.centeringmap[0])/self.blockscale)))] == 0:
                            temp_list_explosion_data.append([explosion_data[i][0]+self.blockscale, explosion_data[i][1], 4, [explosion_data[i][3][0]-1,3]])
                        else:
                            temp_list_explosion_data.append([explosion_data[i][0]+self.blockscale, explosion_data[i][1], 4, [0,3]])
                            collisions_update.append([(int((self.maplimit[0]+1)*((explosion_data[i][1]-self.centeringmap[1])/self.blockscale)+(((explosion_data[i][0]+self.blockscale)-self.centeringmap[0])/self.blockscale))), 0])
                    if explosion_data[i][3][1] == 0 and collisions[(int((self.maplimit[0]+1)*(((explosion_data[i][1]+self.blockscale)-self.centeringmap[1])/self.blockscale)+((explosion_data[i][0]-self.centeringmap[0])/self.blockscale)))] == 0 or explosion_data[i][3][1] == 4 and collisions[(int((self.maplimit[0]+1)*(((explosion_data[i][1]+self.blockscale)-self.centeringmap[1])/self.blockscale)+((explosion_data[i][0]-self.centeringmap[0])/self.blockscale)))] == 0 or explosion_data[i][3][1] == 0 and collisions[(int((self.maplimit[0]+1)*(((explosion_data[i][1]+self.blockscale)-self.centeringmap[1])/self.blockscale)+((explosion_data[i][0]-self.centeringmap[0])/self.blockscale)))] == 2 or explosion_data[i][3][1] == 4 and collisions[(int((self.maplimit[0]+1)*(((explosion_data[i][1]+self.blockscale)-self.centeringmap[1])/self.blockscale)+((explosion_data[i][0]-self.centeringmap[0])/self.blockscale)))] == 2:
                        if collisions[(int((self.maplimit[0]+1)*(((explosion_data[i][1]+self.blockscale)-self.centeringmap[1])/self.blockscale)+((explosion_data[i][0]-self.centeringmap[0])/self.blockscale)))] == 0:
                            temp_list_explosion_data.append([explosion_data[i][0], explosion_data[i][1]+self.blockscale, 4, [explosion_data[i][3][0]-1,4]])
                        else:
                            temp_list_explosion_data.append([explosion_data[i][0], explosion_data[i][1]+self.blockscale, 4, [0,4]])
                            collisions_update.append([(int((self.maplimit[0]+1)*(((explosion_data[i][1]+self.blockscale)-self.centeringmap[1])/self.blockscale)+((explosion_data[i][0]-self.centeringmap[0])/self.blockscale))), 0])

                if explosion_data[i][2] > 0:
                    explosion_data[i][2] -= 1
                    temp_list_explosion_data.append(explosion_data[i])

                
        return temp_list_explosion_data, collisions_update
        