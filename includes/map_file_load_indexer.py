<<<<<<< HEAD
def map_file_indexer(script_path, listdir, Image, Unpickler):
    script_path = script_path.replace("\\", "/")

    fichiers = listdir(f"{script_path}/levels") #Liste les niveaux stocké dans le dossier levels, et seulement ceux qui contiennent .data dans leur nom
    # print(listdir("levels"))
    temp = []
    for i in range(len(fichiers)):
        if fichiers[i].endswith(".data") == True:
            temp.append(fichiers[i][:fichiers[i].find(".data")])
    fichiers = temp

    
    referenced_minimap = listdir(f"{script_path}/img/temp/mini_map")
    temp = []
    for i in range(len(referenced_minimap)):
        if referenced_minimap[i].endswith("_cache.png") == True:
            temp.append(referenced_minimap[i][:referenced_minimap[i].find("_cache.png")])
    referenced_minimap = temp

    print(fichiers, referenced_minimap)

    tempfichiers = []
    for b in range(len(fichiers)):
        founded = False
        check = False
        for k in range(len(referenced_minimap)):
            if fichiers[b] == referenced_minimap[k]:
                founded = True
                tempfichiers.append(fichiers[b])
        
        if founded == False:
            try: #Détecte si le fichier a été suprimé, ou si le fichier ne fini pas par l'extension .data
                with open(f"{script_path}/levels/{fichiers[b]}.data", "rb") as lvl:
                    get_record = Unpickler(lvl)
                    try: #Detecte si le fichier n'est pas une liste
                        lvl_data = get_record.load()
                    except:
                        print("echec de la copie du fichier")
            except:
                print("echec de l'ouverture du fichier")
            try:
                if lvl_data[0] != "MapApprovedCertificate": #Vérifie que la map détient bien a l'occurence 0 le certificat "MapApprovedCertificate" qui permet de s'assurer que ce fichier est lisible en tant que map de jeu
                    print("pas de certificat") #Signale l'absence du certificat et retourne l'erreur comme quoi le fichier est corrompu
                else:
                    check = True
                    # print(f"Valid file : {fichiers[b]}")
            except:
                print("echec de la lecture du certificat") #Si la vérification du certificat echoue

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
                images = [Image.open(x) for x in [f"{script_path}/img/map/ground.png", f"{script_path}/img/map/block.png", f"{script_path}/img/map/break_block.png", f"{script_path}/img/map/wall.png"]]
                line = []
                total_width = blockscale
                max_height = 32
                for i in range(maplimit[1]+1):
                    new_im = Image.new('RGB', (total_width, max_height))
                    x_offset = centeringmapx
                    for k in range(maplimit[0]+1):
                        new_im.paste(images[mapcontent[i*(maplimit[0]+1)+k][0]], (int(x_offset),0))
                        x_offset += 32
                    line.append(new_im)

                max_height = blockscale
                new_im = Image.new('RGB', (total_width, max_height))
                y_offset = centeringmapy
                for i in range(len(line)):
                    new_im.paste(line[i], (0,int(y_offset)))
                    y_offset += 32

                new_im.save(f"{script_path}/img/temp/mini_map/{fichiers[b]}_cache.png")
                tempfichiers.append(fichiers[b])
    
    print(tempfichiers)
=======
def map_file_indexer(script_path, listdir, Image, Unpickler):
    script_path = script_path.replace("\\", "/")

    fichiers = listdir(f"{script_path}/levels") #Liste les niveaux stocké dans le dossier levels, et seulement ceux qui contiennent .data dans leur nom
    # print(listdir("levels"))
    temp = []
    for i in range(len(fichiers)):
        if fichiers[i].endswith(".data") == True:
            temp.append(fichiers[i][:fichiers[i].find(".data")])
    fichiers = temp

    
    referenced_minimap = listdir(f"{script_path}/img/temp/mini_map")
    temp = []
    for i in range(len(referenced_minimap)):
        if referenced_minimap[i].endswith("_cache.png") == True:
            temp.append(referenced_minimap[i][:referenced_minimap[i].find("_cache.png")])
    referenced_minimap = temp

    print(fichiers, referenced_minimap)

    tempfichiers = []
    for b in range(len(fichiers)):
        founded = False
        check = False
        for k in range(len(referenced_minimap)):
            if fichiers[b] == referenced_minimap[k]:
                founded = True
                tempfichiers.append(fichiers[b])
        
        if founded == False:
            try: #Détecte si le fichier a été suprimé, ou si le fichier ne fini pas par l'extension .data
                with open(f"{script_path}/levels/{fichiers[b]}.data", "rb") as lvl:
                    get_record = Unpickler(lvl)
                    try: #Detecte si le fichier n'est pas une liste
                        lvl_data = get_record.load()
                    except:
                        print("echec de la copie du fichier")
            except:
                print("echec de l'ouverture du fichier")
            try:
                if lvl_data[0] != "MapApprovedCertificate": #Vérifie que la map détient bien a l'occurence 0 le certificat "MapApprovedCertificate" qui permet de s'assurer que ce fichier est lisible en tant que map de jeu
                    print("pas de certificat") #Signale l'absence du certificat et retourne l'erreur comme quoi le fichier est corrompu
                else:
                    check = True
                    # print(f"Valid file : {fichiers[b]}")
            except:
                print("echec de la lecture du certificat") #Si la vérification du certificat echoue

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
                images = [Image.open(x) for x in [f"{script_path}/img/map/ground.png", f"{script_path}/img/map/block.png", f"{script_path}/img/map/break_block.png", f"{script_path}/img/map/wall.png"]]
                line = []
                total_width = blockscale
                max_height = 32
                for i in range(maplimit[1]+1):
                    new_im = Image.new('RGB', (total_width, max_height))
                    x_offset = centeringmapx
                    for k in range(maplimit[0]+1):
                        new_im.paste(images[mapcontent[i*(maplimit[0]+1)+k][0]], (int(x_offset),0))
                        x_offset += 32
                    line.append(new_im)

                max_height = blockscale
                new_im = Image.new('RGB', (total_width, max_height))
                y_offset = centeringmapy
                for i in range(len(line)):
                    new_im.paste(line[i], (0,int(y_offset)))
                    y_offset += 32

                new_im.save(f"{script_path}/img/temp/mini_map/{fichiers[b]}_cache.png")
                tempfichiers.append(fichiers[b])
    
    print(tempfichiers)
>>>>>>> 30f25445bfe06d4cfd4ff2dd47a05ad897d6dc15
    return tempfichiers