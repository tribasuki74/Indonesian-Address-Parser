
from database.db import kodePos

class Indonesian_Address_Parser():
    
    def __init__(self, debug=False):
        self.debug = debug
        self.structure = {0: 'PROVINSI', 1: 'KABUPATEN/KOTA', 2: 'KECAMATAN', 3: 'DESA', 4: 'KODEPOS'}
        if self.debug:
            print('Parameters')
            print("=" * 40)
            print('Debug:', self.debug)
            print("=" * 40)
            print()

    def generate_N_grams(text,ngram=1):
        words=[word for word in text.split(" ") if word != ""]  
        temp=zip(*[words[i:] for i in range(0,ngram)])
        ans=[' '.join(ngram) for ngram in temp]
        return ans

    def getKodePos(self, query):
        result = kodePos.find(query)
        if self.debug:
            for a in result:
                print(a)
                print()
        return result

    def parser(self, address = ""):
        pass

    def parser(self, addresses = []):
        pass

        