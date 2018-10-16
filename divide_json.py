import os
import json

with open('task_list.json', 'r') as f:
    json_data = f.read()
data = json.loads(json_data)
print(data)
data1 = data[0:100]
data2 = data[100:]
with open('task_list_1.json', 'w') as e:
    e.write(json.dumps(data1))
with open('task_list_2.json', 'w') as e:
    e.write(json.dumps(data2))
