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

    def res_pos(self, spacex = 0, spacey = 0): # Permet de positionner un élement au meme endroit peu importe la résolution d'affichage
        return round(spacex * self.res[0]/1920) , round(spacey * self.res[1]/1080)

    def load(self, file_name, res, pygame, ground, block, break_block, wall):
        #Verifie que le fichier est utilisable
        try: #Détecte si le fichier a été suprimé, ou si le fichier ne fini pas par l'extension .data
            with open(f"levels/{file_name}.data", "rb") as lvl:
                get_record = pickle.Unpickler(lvl)
                try: #Detecte si le fichier n'est pas une liste
                    lvl_data = get_record.load()
                except:
                    return "Corrupted map" 
        except:
            return "Invalid extension" 
        try:
            if lvl_data[0] != "MapApprovedCertificate": #Vérifie que la map détient bien a l'ocurence 0 le certificat "MapApprovedCertificate" qui permet de s'assurer que ce fichier est lisible en tant que map de jeu
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

        self.texture = [pygame.transform.scale(ground, (self.blockscale,self.blockscale)), 
                        pygame.transform.scale(block, (self.blockscale,self.blockscale)),
                        pygame.transform.scale(break_block, (self.blockscale,self.blockscale)),
                        pygame.transform.scale(wall, (self.blockscale,self.blockscale))]
        
        temp = []
        for i in range(len(self.mapcontent)):
            temp.append([self.mapcontent[i][0], (self.centeringmapx+self.blockscale*self.mapcontent[i][1], self.centeringmapy+self.blockscale*self.mapcontent[i][2])])
        self.mapcontent = temp
        
        return "ok"

    def displayer(self, window_surface, warn):
        for i in range(len(self.mapcontent)):
            window_surface.blit(self.texture[self.mapcontent[i][0]], self.mapcontent[i][1])