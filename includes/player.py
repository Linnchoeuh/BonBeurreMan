class Player():

    def __init__(self, sprite, pos_x, pos_y, length, width, speed):
        
        self.sprite = sprite
        self.x = pos_x
        self.y = pos_y
        self.length = length
        self.width = width
        self.speed = speed

# %%
#test grille
grille = []
for x in range(15+1):
    for y in range(13+1):
        grille.append([x,y])

print(grille)

#coucou