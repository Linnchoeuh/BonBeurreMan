import pickle

class Mapdislayer:
    def __init__(self):
        self.mapcontent = []

    def load(self, file_name):
        try:
            with open(f"levels/{file_name}.data", "rb") as lvl_data:
                get_record = pickle.Unpickler(lvl_data)
                try:
                    map_data = get_record.load()
                except:
                    return "Corrupted map"
        except:
            return "Invalid extension"
        try:
            if map_data[0] != "MapApprovedCertificate":
                return "Corrupted map"
        except:
            return "Corrupted map"
        print(map_data)
        return "ok"
