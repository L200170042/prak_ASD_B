#no.1
def segitiga():
    for i in range(5):
        for j in range(i+1):
            print("*", end=' ')
        print()
    return(i)
segitiga()

#no.2
def persegiEmpat (x,y):
    for i in range (x):
        if i== 0  or i==x-1:
            print ("@"*y)
        else:

            print ("@"+" "*(y-2)+"@")

persegiEmpat(4,5)


#no.3a
def jmlvokal(string):
    vok = 0
    x = "aiueoAIUEO"
    for car in string.lower():
        if car in x:
            vok += 1
    vokal = len(string)
    return(vokal,vok)

#no.3b
def jmlkonso(string):
    vok = 0
    x = "aiueoAIUEO"
    for car in string.lower():
        if car not in x:
            vok += 1
    vokal = len(string)
    return(vokal,vok)

#no.4
def rerata(x):
	"Hitung Rata Rata dari List"
	jml=0
	banyak=0
	for angka in x:
		jml+=angka
		banyak+=1
	return jml/banyak
print(rerata([1,2,3,4,5]))
g = [3,4,5,4,3,4,5,2,2,10,11,23]
rerata(g)

#no.5
from math import sqrt as sq
def apakahPrima(n):
    n=int(n)
    assert n>=0
    primakecil=[2, 3, 5, 7, 11]
    bukanprima=[0, 1, 4, 6, 8, 9, 10]
    if n in primakecil:
        return True
    elif n in bukanprima:
        return False
    else:
        for i in range(2,int(sq(n))+1):
            if(n%i==0):
                return False
    return True
print(apakahPrima(17))
print(apakahPrima(97))
print(apakahPrima(123))

#no.6
def bilanganprima():
    prima=list()
    for i in range(2,1000):
        a = True
        for angka in prima:
            if(i%angka==0):
                a=False
                break
        if(a):
            print(i)
            prima.append(i)
bilanganprima()

##no.7
def faktorprima(n):
    prima=list()
    for x in range(2,n):
        a = True
        for iter in prima:
            if(x%iter==0):
                a=False
                break
        if a and n%x==0:
            prima.append(x)
    return prima
print(faktorprima(143))
print(faktorprima(10))
print(faktorprima(19))

###no.8
def apakahTerkandung(a,b):
    return a in b
print(apakahTerkandung("do","Indonesia tanah air beta"))
print(apakahTerkandung("pusaka","Indonesia tanah air beta"))

##no.9
def iterasi():
    for x in range(1,100):
        if (x%3)!=0 and (x%5)!=0:
            print(x)
        else:
            if (x%15)==0:
                print("pyton UMS")
            elif (x%3)==0:
                print("python")
            elif (x%5)==0:
                print("UMS")
iterasi()

##no.10
def selesaikanABC(a,b,c):
    a=float(a)
    b=float(b)
    c=float(c)
    D=(b**2)-(4*a*c)
    if D<0:
        return "determinan negatif"
    return  "determinan positif"
print(selesaikanABC(1,2,3))

##no.11
def apakahkabisat(x):
    if(x%400==0):
        return True
    if(x%100==0):
        return False
    if(x%4==0):
        return True
    return False
print(apakahkabisat(100))

##no.12
import random
def permainan():
    a=random.randrange(0, 100)
    while(True):
        b=int(input("masukan angka: "))
        if(b>a):
            print("terlalu besar, coba lagi")
        elif(b<a):
            print("terlalu kecil, coba lagi")
        else:
            print("benar")
            break
permainan()

##no.13
def katakan(angka):
    satuan = ["satu", "dua", "tiga", "empat", "lima",
              "enam", "tujuh", "delapan", "sembilan", "sepuluh",
              "sebelas", "dua belas", "tiga belas", "empat belas", "lima belas",
              "enam belas", "tujuh belas", "delapan belas", "sembilan belas"
              ]
    angka = '{:0,.0f}'.format(int(angka))
    angka = angka.split(",")
    katakan = []
    idx = 1
    for x in angka[::-1]:
        seribu = False
        if idx == 2 and x[-1]!="0":
            if int(x)< 2 :
                katakan.append("seribu")
                seribu = True
            else:
                katakan.append("ribu")
        if idx == 3 and x[-1]!="0":
            katakan.append("juta")
        if seribu == False:
            if int(x[-2:])<20 and int(x[-2:])>0:
                katakan.append(satuan[int(x[-2:])-1])
            elif int(x[-2:])>0:
                if int(x[-1])!=0:
                    katakan.append(satuan[int(x[-1])-1])
                if int(x[-2]) != 0:
                    katakan.append(satuan[int(x[-2])-1]+" puluh")
        if int(x[0]) > 2 and len(x)==3 :
            katakan.append(satuan[int(x[0])-1]+" ratus")
        elif len(x)==3 and int(x[0])!=0 :
            katakan.append("seratus")
        idx+=1
    return " ".join(katakan[::-1])

print(katakan(3125750))

##no.14
def formatRupiah(n):
    x = '{:,}'.format(n).replace(',', '.')
    return "Rp " + x
print(formatRupiah(300000))
