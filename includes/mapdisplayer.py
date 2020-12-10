import pickle

class Mapdislayer:
    def __init__(self, res):
        self.mapcontent = []
        self.maplimit = [0, 0]
        self.playersspawns = [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]
        self.centeringmapx = 0
        self.centeringmapy = 0
        self.blockscale = 0
        self.res = res
        self.texture = []
        self.bg_map = 0
        self.collisionsmap = [] #0 pas de collisions, 1 collisions, 2 block cassable, 3 joueur, 4 bomb, 5 power up

    def res_pos(self, spacex = 0, spacey = 0): # Permet de positionner un élement au meme endroit peu importe la résolution d'affichage
        return round(spacex * self.res[0]/1920) , round(spacey * self.res[1]/1080)

    def load(self, file_name, res, pygame, Image, script_path, Unpickler, ground, block, break_block, wall):
        #Verifie que le fichier est utilisable
        try: #Détecte si le fichier a été suprimé, ou si le fichier ne fini pas par l'extension .data
            with open(f"{script_path}/levels/{file_name}.data", "rb") as lvl:
                get_record = Unpickler(lvl)
                try: #Detecte si le fichier n'est pas une liste
                    lvl_data = get_record.load()
                except:
                    return "Corrupted map" 
        except:
            return "Invalid extension" 
        try:
            if lvl_data[0] != "MapApprovedCertificate": #Vérifie que la map détient bien a l'occurence 0 le certificat "MapApprovedCertificate" qui permet de s'assurer que ce fichier est lisible en tant que map de jeu
                return "Corrupted map" #Signale l'absence du certificat et retourne l'erreur comme quoi le fichier est corrompu
        except:
            return "Corrupted map" #Si la vérification du certificat echoue
        
        self.maplimit = [lvl_data[1], lvl_data[2]] #Stocke la taille de la map
        self.playersspawns = lvl_data[3] #Stocke les spawn des joueurs
        self.mapcontent = lvl_data[4:] #Stocke les élement de la map
        temp = []
        for i in range(len(self.mapcontent)): #vérifie que la liste ne contient pas d'élément qui dépasse de la carte, et les retire le cas echeant
            if self.mapcontent[i][1] <= self.maplimit[0] and self.mapcontent[i][2] <= self.maplimit[1]:
                temp.append(self.mapcontent[i])
        
        self.mapcontent = [] #trie et rempli les cases n'ayant pas été référencé par du sol
        for i in range(self.maplimit[1]+1):
            for k in range(self.maplimit[0]+1):
                block_exist = False
                for a in range(len(temp)):
                    if temp[a] == [temp[a][0], k, i]:
                        self.mapcontent.append(temp[a])
                        block_exist = True
                        break
                if block_exist == False:
                    self.mapcontent.append([0, k, i])
        if 1920/(self.maplimit[0]+1) < 1080/(self.maplimit[1]+1):
            self.blockscale = int(res[0]/(self.maplimit[0]+1))
            self.centeringmapx = 0
            self.centeringmapy = res[1]/2-(self.blockscale*(self.maplimit[1]+1))/2
        else:
            self.blockscale = int(res[1]/(self.maplimit[1]+1))
            self.centeringmapx = res[0]/2-(self.blockscale*(self.maplimit[0]+1))/2
            self.centeringmapy = 0

        self.texture = [pygame.transform.scale(break_block, (self.blockscale,self.blockscale))
                        ]
        self.collisionsmap = []
        for i in range(len(self.mapcontent)):
            if self.mapcontent[i][0] == 1 or self.mapcontent[i][0] == 3:
                self.collisionsmap.append(1)
            elif self.mapcontent[i][0] == 2:
                self.collisionsmap.append(2)
            else:
                self.collisionsmap.append(0)
        print(self.collisionsmap)

        temp = []
        for i in range(len(self.mapcontent)):
            if self.mapcontent[i][0] == 2:
                temp.append([0, (self.centeringmapx+self.blockscale*self.mapcontent[i][1], self.centeringmapy+self.blockscale*self.mapcontent[i][2])])
            # elif self.mapcontent[i][0] == 4:
            #     self.mapcontent.append([1, (self.centeringmapx+self.blockscale*self.mapcontent[i][1], self.centeringmapy+self.blockscale*self.mapcontent[i][2])])
        images = [Image.open(x) for x in [f"{script_path}/img/map/ground.png", f"{script_path}/img/map/block.png", f"{script_path}/img/map/wall.png"]]
        line = []
        total_width = (self.maplimit[0]+1)*32
        max_height = 32
        for i in range(self.maplimit[1]+1):
            new_im = Image.new('RGB', (total_width, max_height))
            x_offset = 0   
            for k in range(self.maplimit[0]+1):
                if self.mapcontent[i*(self.maplimit[0]+1)+k][0] == 1:
                    new_im.paste(images[1], (x_offset,0))
                elif self.mapcontent[i*(self.maplimit[0]+1)+k][0] == 3:
                    new_im.paste(images[2], (x_offset,0))
                else:
                    new_im.paste(images[0], (x_offset,0))
                x_offset += 32
            line.append(new_im)
        
        max_height = (self.maplimit[1]+1)*32
        new_im = Image.new('RGB', (total_width, max_height))
        y_offset = 0
        for i in range(len(line)):
            new_im.paste(line[i], (0,y_offset))
            y_offset += 32

        new_im.save(f"{script_path}/img/temp/cache.png")
        
        self.bg_map = pygame.image.load(f"{script_path}/img/temp/cache.png")
        self.bg_map = pygame.transform.scale(self.bg_map, (int(total_width*(self.blockscale/32)), int(max_height*(self.blockscale/32))))
        images = 0
        new_im = 0
        self.mapcontent = temp
        
        return "ok"

    # type de block : (si le block n'est pas renseigné il sera remplacé par un ground)
    # 0 = ground
    # 1 = block solid
    # 2 = block breakable
    # 3 = wall
    # 4 = power-up
    def displayer(self, window_surface, warn):
        window_surface.blit(self.bg_map, (self.centeringmapx, self.centeringmapy))
        for i in range(len(self.mapcontent)):
            window_surface.blit(self.texture[self.mapcontent[i][0]], self.mapcontent[i][1])
    
    def collisions_updater(self, modification):
        if modification != []:
            pass
        return self.collisionsmap