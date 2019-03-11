#no.2
class Mahasiswa(object):
    """class mahasiswa yang dibangun dari class mahasiswa."""
    def __init__(self, nama, NIM, kota, us):
        """metode menutupi inisialisasi di class manusia."""
        self.nama = nama
        self.NIM = NIM
        self.kota = kota
        self.uangsaku = us
    def __str__(self):
        s = self.nama +', NIM' +str(self.NIM) \
            +', tinggal di ' + self.kota \
            +', uang saku Rp. ' +str(self.uangsaku) \
            +' tiap bulan.'
        return s
    def ambilnama(self):
        return self.nama
    def ambilNIM(self):
        return self.NIM
    def ambiluangsaku(self):
        return self.uangsaku
    def makan(self, s):
        """metode ini menutupi metode 'makan' calss manusia.
            mahasiswa kalau makan sambil belajar."""
        print("saya baru saja makan",s,"sambil belajar.")
        self.keadaan = "kenyang"

#2a
    def kotatinggal(self):
        return self.kota
#2b
    def perbarui(self,stringBaru):
        self.kota = stringBaru
#2c
    def tambahuangsaku(self, tambah):
        self.uangsaku +=tambah
        
