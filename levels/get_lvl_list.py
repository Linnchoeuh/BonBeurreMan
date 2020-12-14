from pickle import Unpickler
from os.path import dirname, realpath

script_path = dirname(realpath(__file__))
script_path = script_path.replace("\\", "/")

name = input("Donnez le nom du fichier: ")

try:
    with open(f"{script_path}/{name}.data", "rb") as lvl:
        get_record = Unpickler(lvl)
        got = get_record.load()

    print(f'["{got[0]},"')
    for i in range(len(got)-2):
        print(f"{got[i+1]},")
    print(f"{got[-1]}]")

    input("Terminé")
except:
    input("Le fichier n'existe pas.")
