class MhsTIF(object):
    def __init__(self, nama, umur, kota, NIM):
        self.nama = nama
        self.umur = umur
        self.kotaTinggal = kota
        self.nim = NIM

    def __str__(self):
        x = self.nim
        return x

    def getnim(self):
        return self.nim

c0 = MhsTIF('Ika', 10, 'Sukoharjo', 'L200170044')
c1 = MhsTIF('Budi', 14, 'Klaten', 'L200170048')
c2 = MhsTIF('Ahmad', 12, 'Surakarta', 'L200170047')
c3 = MhsTIF('Chandra', 21, 'Wonogiri', 'L200170046')
c4 = MhsTIF('Rossy', 20, 'Salatiga', 'L200170042')
c5 = MhsTIF('Fandi', 65, 'Purworejo', 'L200170041')
c6 = MhsTIF('Hasan', 11, 'Bandung', 'L200170045')
c7 = MhsTIF('Galuh', 43, 'Surabaya', 'L200170049')
c8 = MhsTIF('Deni', 56, 'Purwodadi', 'L200170039')
c9 = MhsTIF('Danis', 6, 'Salatiga', 'L200170040')
c10 = MhsTIF('Risa', 20, 'Purwodadi', 'L200170038')

Daftar = [c0, c1, c2, c3, c4, c5, c6, c7, c8, c9, c10]

def insertionSort(A):
    n = len(A)
    for i in range(1, n):
        nilai = A[i]
        pos = i
        while pos > 0 and nilai.nim < A[pos - 1].nim:
            A[pos] = A[pos - 1]
            pos = pos - 1
        A[pos] = nilai

def cetakDaftar(d):
    for i in d:
        print (i)
        
insertionSort(Daftar)
cetakDaftar(Daftar)
