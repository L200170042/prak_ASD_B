import re


#No 2
a = open("Indonesia.txt","r")
teks = a.read()
cocok = r' di\w+'
output = re.findall(cocok,teks)
for i in output :
    print (i[1:])
a.close()
