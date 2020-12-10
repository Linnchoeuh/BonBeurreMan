class MapEditor():
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

    def load(self, file_name, res, pygame, script_path, Unpickler, ground, block, break_block, wall):
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
        if 1920/(self.maplimit[0]+1) < 1080/(self.maplimit[1]+1):
            self.blockscale = int(self.res[0]/(self.maplimit[0]+1)/1.1)
            self.centeringmapx = 0
            self.centeringmapy = self.res[1]/2-(self.blockscale*(self.maplimit[1]+1))/2
        else:
            self.blockscale = int(self.res[1]/(self.maplimit[1]+1)/1.1)
            self.centeringmapx = self.res[0]/2-(self.blockscale*(self.maplimit[0]+1))/2
            self.centeringmapy = 0
        self.mapcontent = [] #trie et rempli les cases n'ayant pas été référencé par du sol
        for i in range(self.maplimit[1]+1):
            for k in range(self.maplimit[0]+1):
                block_exist = False
                for a in range(len(temp)):
                    if temp[a] == [temp[a][0], k, i]:
                        self.mapcontent.append([temp[a][0], (self.centeringmapx+self.blockscale*temp[a][1], self.centeringmapy+self.blockscale*temp[a][2])])
                        block_exist = True
                        break
                if block_exist == False:
                    self.mapcontent.append([0, (self.centeringmapx+k*self.blockscale, self.centeringmapy+i*self.blockscale)])
        

        # print(self.mapcontent)
        self.texture = [pygame.transform.scale(ground, (self.blockscale,self.blockscale)),
                        pygame.transform.scale(block, (self.blockscale,self.blockscale)),
                        pygame.transform.scale(break_block, (self.blockscale,self.blockscale)),
                        pygame.transform.scale(wall, (self.blockscale,self.blockscale))
                        ]

    def displayer(self, window_surface):
        
        for i in range(len(self.mapcontent)):
            window_surface.blit(self.texture[self.mapcontent[i][0]], self.mapcontent[i][1])

    def mapmodifier(self, mx, my):
        pass


"""level = ["MapApprovedCertificate", 29, 29, [[1,1],[28,28],[28,1],[1,28],[15,1],[28,15],[15,28],[1,15]],   #Taille de la map x, Taille de la map y, positions d'apparition de chaque joueur
#Contour de la map
[3, 0, 0], #type de block, x, y
[3, 1, 0],
[3, 2, 0],
[3, 3, 0],
[3, 4, 0],
[3, 5, 0],
[3, 6, 0],
[3, 7, 0],
[3, 8, 0],
[3, 9, 0],
[3, 10, 0],
[3, 11, 0],
[3, 12, 0],
[3, 13, 0],
[3, 14, 0],
[3, 15, 0],
[3, 16, 0],
[3, 17, 0],
[3, 18, 0],
[3, 19, 0],
[3, 20, 0],
[3, 21, 0],
[3, 22, 0],
[3, 23, 0],
[3, 24, 0],
[3, 25, 0],
[3, 26, 0],
[3, 27, 0],
[3, 28, 0],
[3, 29, 0],

[3, 29, 1],
[3, 29, 2],
[3, 29, 3],
[3, 29, 4],
[3, 29, 5],
[3, 29, 6],
[3, 29, 7],
[3, 29, 8],
[3, 29, 9],
[3, 29, 10],
[3, 29, 11],
[3, 29, 12],
[3, 29, 13],
[3, 29, 14],
[3, 29, 15],
[3, 29, 16],
[3, 29, 17],
[3, 29, 18],
[3, 29, 19],
[3, 29, 20],
[3, 29, 21],
[3, 29, 22],
[3, 29, 23],
[3, 29, 24],
[3, 29, 25],
[3, 29, 26],
[3, 29, 27],
[3, 29, 28],
[3, 29, 29],

[3, 1, 29],
[3, 2, 29],
[3, 3, 29],
[3, 4, 29],
[3, 5, 29],
[3, 6, 29],
[3, 7, 29],
[3, 8, 29],
[3, 9, 29],
[3, 10, 29],
[3, 11, 29],
[3, 12, 29],
[3, 13, 29],
[3, 14, 29],
[3, 15, 29],
[3, 16, 29],
[3, 17, 29],
[3, 18, 29],
[3, 19, 29],
[3, 20, 29],
[3, 21, 29],
[3, 22, 29],
[3, 23, 29],
[3, 24, 29],
[3, 25, 29],
[3, 26, 29],
[3, 27, 29],
[3, 28, 29],

[3, 0, 1],
[3, 0, 2],
[3, 0, 3],
[3, 0, 4],
[3, 0, 5],
[3, 0, 6],
[3, 0, 7],
[3, 0, 8],
[3, 0, 9],
[3, 0, 10],
[3, 0, 11],
[3, 0, 12],
[3, 0, 13],
[3, 0, 14],
[3, 0, 15],
[3, 0, 16],
[3, 0, 17],
[3, 0, 18],
[3, 0, 19],
[3, 0, 20],
[3, 0, 21],
[3, 0, 22],
[3, 0, 23],
[3, 0, 24],
[3, 0, 25],
[3, 0, 26],
[3, 0, 27],
[3, 0, 28],
[3, 0, 29],
]


name = "oui"
with open(f"levels/{name}.data", "wb") as lvl:
    record = pickle.Pickler(lvl)
    record.dump(level)

print("File created with success")"""
