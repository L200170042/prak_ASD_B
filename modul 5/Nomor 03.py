##c0 = MhsTIF('ika', 10, 'Sukoharjo', 240000)
##c1 = MhsTIF('Budi', 51, 'Sragen', 250000)
##c2 = MhsTIF('Ahmad', 2, 'Surakarta', 250000)
##c3 = MhsTIF('Chandra', 18, 'Surakarta', 235000)
##c4 = MhsTIF('Eka', 4, 'Boyolali', 240000)
##c5 = MhsTIF('Fandi', 31, 'Salatiga', 250000)
##c6 = MhsTIF('Deni', 13, 'Klaten', 245000)
##c7 = MhsTIF('Galuh', 5, 'Wonogiri', 245000)
##c8 = MhsTIF('Janto', 23, 'Klaten', 245000)
##c9 = MhsTIF('Hasan', 64, 'Karanganyar', 270000)
##c10 = MhsTIF('Khalid', 29, 'Purwodadi', 265000)
##
##daftar = [c0, c1, c2, c3, c4, c5, c6, c7, c8, c9, c10]
def swap(A,p,q):
    tmp = A[p]
    A[p] = A[q]
    A[q] = tmp

def selectionSort(A):
    n = len(A)
    for i in range(n - 1):
        indexkecil = cariposisiyangterkecil(A, i, n)
        if indexkecil != 1:
            swap(A, i, indexkecil)

def insertionSort(A):
    n = len(A)
    for i in range(1, n):
        nilai = A[i]
        pos = i
        while pos > 0 and nilai < A[pos - 1]:
            A[pos] = A[pos - 1]
            pos = pos -1
        A[pos] = nilai

def cariposisiyangterkecil(A, darisini, sampaisini):
    posisiyangterkecil = darisini
    for i in range(darisini+1, sampaisini):
        if A[i] < A[posisiyangterkecil]:
            posisiyangterkecil = i
    return posisiyangterkecil


            
def bubbleSort(A):
    n = len (A)
    for i in range (n-1):
        for j in range (n-i-1):
            if A[j] > A[j+1]:
                swap(A,j,j+1)

from time import time as detak
from random import shuffle as kocok
k = [i for i in range(1,6001)]
kocok(k)
u_bub = k[:]
u_sel = k[:]
u_ins = k[:]

aw = detak();bubbleSort(u_bub); ak=detak();print('bubble : %g detik' %(ak-aw));
aw = detak();selectionSort(u_sel); ak=detak();print('Selection : %g detik' %(ak-aw));
aw = detak();insertionSort(u_ins); ak=detak();print('insertion : %g detik' %(ak-aw));
