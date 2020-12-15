import pickle
# type de block : (si le block n'est pas renseigné il sera remplacé par un ground)
# 0 = ground
# 1 = block solid
# 2 = block breakable
# 3 = wall
# 4 = power-up
# Taille de la map x, Taille de la map y, positions d'apparition de chaque joueur
# Type de block, x, y
level = ["MapApprovedCertificate",
14,
10,
[[1, 5], [13, 5]],
[3, 0, 0],
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

[3, 1, 0],
[3, 2, 0],
[3, 3, 0],
[3, 4, 0],
[3, 5, 0],
[3, 6, 0],

[3, 6, 1],
[3, 8, 1],
[3, 6, 2],
[3, 7, 2],
[3, 8, 2],

[3, 8, 0],
[3, 9, 0],
[3, 10, 0],
[3, 11, 0],
[3, 12, 0],
[3, 13, 0],

[3, 14, 0],
[3, 14, 1],
[3, 14, 2],
[3, 14, 3],
[3, 14, 4],
[3, 14, 5],
[3, 14, 6],
[3, 14, 7],
[3, 14, 8],
[3, 14, 9],
[3, 14, 10],

[3, 1, 10],
[3, 2, 10],
[3, 3, 10],
[3, 4, 10],
[3, 5, 10],
[3, 6, 10],

[3, 6, 9],
[3, 8, 9],
[3, 6, 8],
[3, 7, 8],
[3, 8, 8],

[3, 8, 10],
[3, 9, 10],
[3, 10, 10],
[3, 11, 10],
[3, 12, 10],
[3, 13, 10],

[1, 2, 2],
[1, 4, 2],
[1, 2, 4],
[1, 4, 4],
[1, 2, 6],
[1, 4, 6],
[1, 2, 8],
[1, 4, 8],

[1, 10, 2],
[1, 12, 2],
[1, 10, 4],
[1, 12, 4],
[1, 10, 6],
[1, 12, 6],
[1, 10, 8],
[1, 12, 8],

[1, 7, 6],
[1, 7, 4],


[2, 1, 1],
[2, 1, 2],
[2, 1, 3],
[2, 1, 7],
[2, 1, 8],
[2, 1, 9],

[2, 2, 1],
[2, 2, 3],
[2, 2, 7],
[2, 2, 9],

[2, 3, 1],
[2, 3, 2],
[2, 3, 3],
[2, 3, 4],
[2, 3, 5],
[2, 3, 6],
[2, 3, 7],
[2, 3, 8],
[2, 3, 9],

[2, 4, 1],
[2, 4, 3],
[2, 4, 5],
[2, 4, 7],
[2, 4, 9],

[2, 5, 1],
[2, 5, 2],
[2, 5, 3],
[2, 5, 4],
[2, 5, 5],
[2, 5, 6],
[2, 5, 7],
[2, 5, 8],
[2, 5, 9],

[2, 6, 3],
[2, 6, 4],
[2, 6, 5],
[2, 6, 6],
[2, 6, 7],

[2, 7, 3],
[2, 7, 7],

[2, 8, 3],
[2, 8, 4],
[2, 8, 5],
[2, 8, 6],
[2, 8, 7],

[2, 9, 1],
[2, 9, 2],
[2, 9, 3],
[2, 9, 4],
[2, 9, 5],
[2, 9, 6],
[2, 9, 7],
[2, 9, 8],
[2, 9, 9],

[2, 10, 1],
[2, 10, 3],
[2, 10, 5],
[2, 10, 7],
[2, 10, 9],

[2, 11, 1],
[2, 11, 2],
[2, 11, 3],
[2, 11, 4],
[2, 11, 5],
[2, 11, 6],
[2, 11, 7],
[2, 11, 8],
[2, 11, 9],

[2, 12, 1],
[2, 12, 3],
[2, 12, 7],
[2, 12, 9],

[2, 13, 1],
[2, 13, 2],
[2, 13, 3],
[2, 13, 7],
[2, 13, 8],
[2, 13, 9]
]


with open("levels/test.data", "wb") as lvl:
    record = pickle.Pickler(lvl)
    record.dump(level)

print("File created with success")