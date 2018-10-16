import json
import multiprocessing
from base_download import TrackSamImage, DownloadSamTask

# ss = []
# with open('/data/deeplearning/out/1.json', 'r') as f:
#     json_data = json.loads(f.read())
# print(type(json_data))
# for k, v in json_data.items():
#     for i in v:
#         if i['name'] == 'IMGADD':
#             ss.append(i['value'])

track_handler = TrackSamImage()
manager = multiprocessing.Manager()
download_queue = manager.Queue()
# count_queue = manager.Queue()
ss = ['38867_20180824153326994331']

print(len(ss))

#
# for url in ss:
#t = url.split('&')
#r = t[0].split('?')
#s = r[1].split("=")
for i in ss:
    download_task = DownloadSamTask(trackPointId=i)
    download_queue.put(download_task)
    # count_queue.put(1)

for x in range(32):
    download_task = DownloadSamTask(trackPointId=None, exit_flag=True)
    download_queue.put(download_task)
download_procs = []

for x in range(32):
    download_proc = multiprocessing.Process(target=track_handler.download_image, args=(download_queue,))
    download_proc.daemon = True
    download_procs.append(download_proc)

for proc in download_procs:
    proc.start()
# count = multiprocessing.Process(target=self.update_task, args=(count_queue,))
# count.start()

for proc in download_procs:
    proc.join()
# count.join()
