from pickle import Unpickler
from os.path import dirname, realpath

script_path = dirname(realpath(__file__))
script_path = script_path.replace("\\", "/")

name = input("Donnez le nom du fichier: ")

try:
    with open(f"{script_path}/{name}.data", "rb") as lvl:
        get_record = Unpickler(lvl)
        got = get_record.load()

    with open(f"{script_path}/level_list_return.txt", "w") as a:
        a.write("[")
        for i in range(len(got)-1):
            a.write(f"{got[i]},\n")
        a.write(f"{got[-1]}]")

    input("Terminé")
except:
    input("Le fichier n'existe pas.")



