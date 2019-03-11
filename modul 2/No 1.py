#no 1
class pesan(object):
    """
        sebuah class bernama pesan.
        untuk memahami konsep class dan object.
    """
    def __init__(self, sebuahString):
        self.teks = sebuahString
    def cetakIni(self):
        print(self.teks)
    def cetakHurufkapital(self):
        print(str.upper(self.teks))
    def cetakHurufkecil(self):
        print(str.lower(self.teks))
    def jamKar(self):
        return len(self.teks)
    def cetakJumlahKarakterku(self):
        print('kalimatku mempunyai' ,len(self.teks),'karakter.')
    def perbarui(self,stringBaru):
        self.teks = stringBaru
        
#1a
    def apakahterkandung(self, string):
        return string in self.teks
#1c   
    def hitungvokal(self):
        vok = 0
        x = "aiueoAIUEO"
        for car in self.teks:
            if car in x:
                vok += 1
        return(vok)
#1b
    def hitungkonsonan(self):
        vok = 0
        x = "aiueoAIUEO"
        for car in self.teks:
            if car not in x:
                vok += 1
        return(vok)
