import requests
import json

task_ids = []
for id in range(171763, 172762):
    id = str(id)
    url = 'http://10.11.5.74:13320/kms/history/historic-process-instances?includeProcessVariables=true&businessKey={}'.format(
        id)
    req_data = requests.get(url)
    req_text = json.loads(req_data.text)
    datas = req_text['data'][0]
    task_id = datas["id"]
    print(task_id)
    task_ids.append(task_id)
print task_ids
for del_id in task_ids:
    url = 'http://10.11.5.74:13320/kms/runtime/process-instances/{}'.format(
        del_id)
    req_data = requests.delete(url)
