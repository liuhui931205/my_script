import json
import requests

track_point_id = []
ids = [3590579]

for id in ids:
    try:
        url = 'http://192.168.7.27:13320/kms/runtime/process-instances/{}/variables'.format(id)
        req_data = requests.get(url=url)
        req_data = json.loads(req_data.text)
        for i in req_data:
            if i['name'] == 'TRACKPOINTID':
                track_point_id.append(i['value'])
    except Exception as e:
        print(e, id)

print(len(track_point_id))
print(track_point_id)
