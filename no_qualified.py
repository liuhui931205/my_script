import re
import json

li = []
with open('1.txt', 'r') as f:
    data = f.readlines()
for line in data:
    matc = re.findall(r'\d{5}/label-.*png', line)
    li.append(matc)
print(li)
with open('3.csv', 'w') as f2:
    s = {}
    for i in li:
        w = i[0].split('/')
        _str = "{},{}\n".format(w[0], w[1])
        f2.write(_str)
