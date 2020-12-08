import pickle

class Mapdislayer:
    def __init__(self):
        self.mapcontent = []
        self.maplimit = [0, 0]
        self.playersspawns = [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]
        self.centeringmap = 0
        self.blockscale = 0


    def load(self, file_name, res):
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
        a = 0
        self.mapcontent = [] #trie et rempli les cases n'ayant pas été référencé par du sol
        for i in range(self.maplimit[1]+1):
            for k in range(self.maplimit[0]+1):
                # print(f"compare {temp[a]} | {[temp[a][0], i, k]}")
                if temp[a] == [temp[a][0], i, k]:
                    self.mapcontent.append(temp[a])
                    # print(True)
                else:
                    self.mapcontent.append([0, i, k])
            a += 1
        if 1920/(self.maplimit[0]+1) < 1080/(self.maplimit[1]+1):
            self.blockscale = (1920/(self.maplimit[0]+1)) * res[0]/1920
            self.centeringmap = 0
            # print("x")
        else:
            self.blockscale = (1080/(self.maplimit[1]+1)) * res[1]/1080
            self.centeringmap = res[0]/2-((self.maplimit[0]+1)*self.blockscale)/2
            # print("y")

        
        # print(self.blockscale, self.centeringmap)
        
        return "ok"
