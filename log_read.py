import re

with open('kddata_cls14_germany.train.log.germanyup02', 'r') as f:
    data = f.readlines()
li = []
lis = []
nd = []
for i in data:
    # m = re.findall(r'base_module.*Epoch\[\d+\]', i)
    m = re.findall(r"base_module.*Train-mean-iou=\d+\.\d+", i)
    if m:
        li.append(m)
for j in li:
    n = j[0].split('=')
    d = re.findall(r'\d+', n[0])
    lis.append(n[-1])
    nd.append(d[-1])
print(lis)
print(nd)
