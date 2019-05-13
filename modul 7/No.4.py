import re

#No 4
f = open("KEI.html","r")
teks = f.read()
f.close()
cocok = r'([\w+]+)</a></td>\
<td>\d\.\d\d</td>\
<td>\d\.\d\d</td>\
<td>\d\.\d\d</td>\
<td>([\d.\d\d]+)'
output = re.findall(cocok,teks)
print(output)
