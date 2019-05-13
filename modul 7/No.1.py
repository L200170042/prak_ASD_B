import re


#no 1
a = open("Indonesia.txt","r",encoding="latin1")
teks = a.read()
cocok = r'me\w+'
output = re.findall(cocok,teks)
for i in output :
    print (i[1:])
a.close()
