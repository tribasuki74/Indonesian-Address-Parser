
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

    def getProvinsi(self, _list):
        pr = []
        for i in _list:
            exist = False
            for idx, p in enumerate(pr):
                if i[0] == p[0]:
                    exist = True
                    if i[1] > p[1]:
                        p[1] = i[1]
                    p[2] = p[2] + 1
            
            if not exist:
                pr.append([i[0], i[1], 1])   
        return pr

    def sort(self, subLi):
        sub_li = getProvinsi(subLi)
        print(sub_li)
        l = len(sub_li)
        for i in range(0, l):
            for j in range(0, l-i-1):
                if (sub_li[j][1] < sub_li[j + 1][1]):
                    tempo = sub_li[j]
                    sub_li[j]= sub_li[j + 1]
                    sub_li[j + 1]= tempo
                if (sub_li[j][1] == sub_li[j + 1][1]):
                    if (sub_li[j][2] < sub_li[j + 1][2]):
                        tempo = sub_li[j]
                        sub_li[j]= sub_li[j + 1]
                        sub_li[j + 1]= tempo
        return sub_li

    

    def generate_N_grams(self, text,ngram=1):
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

        