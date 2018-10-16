import os
import requests
import time
import cv2
import numpy as np


class DownloadSamTask:
    def __init__(self, trackPointId, exit_flag=False):
        self.trackPointId = trackPointId
        self.exit_flag = exit_flag


class TrackSamImage:
    def __init__(self):
        self.total_count = 0

    @staticmethod
    def download_image(download_queue):
        while True:
            if download_queue.empty():
                time.sleep(3)

            download_task = download_queue.get()
            if not isinstance(download_task, DownloadSamTask):
                break

            if download_task.exit_flag:
                break

            trackpointid = download_task.trackPointId
            try:
                url1 = "http://192.168.7.27:13100/krs/image/get?trackPointId={}&type=00&seq=004&imageType=jpg".format(
                    trackpointid)
                url2 = "http://192.168.7.27:13100/krs/image/get?trackPointId={}&type=70&seq=001&imageType=png".format(
                    trackpointid)
                s = [url1, url2]
                for i in s:
                    res_data = requests.get(url=i)
                    content_type = res_data.headers['Content-Type']
                    if not str(content_type).startswith("image"):
                        print("Download  from failed:%s" % i)
                    else:
                        origin_image_data = res_data.content
                        _image0 = np.asarray(bytearray(origin_image_data), dtype="uint8")
                        origin_image = cv2.imdecode(_image0, cv2.IMREAD_COLOR)

                        width = origin_image.shape[1]
                        height = origin_image.shape[0]

                        blank_image = np.zeros((height, width, 3), np.uint8)
                        blank_image[0:height, 0:width] = (255, 255, 255)
                        blank_image[0:height, 0:width] = origin_image

                        if s[0] == i:
                            img_array = cv2.imencode('.jpg', blank_image)
                            img_data = img_array[1]
                            image_data = img_data.tostring()
                            dir_name = '{}_00_004.jpg'.format(trackpointid)
                        else:
                            img_array = cv2.imencode('.png', blank_image)
                            img_data = img_array[1]
                            image_data = img_data.tostring()
                            dir_name = 'label-{}_00_004.png'.format(trackpointid)
                        with open(
                                os.path.join('/data/deeplearning/dataset/training/data/released/test', dir_name),
                                "wb") as f:
                            f.write(image_data)
            except Exception as e:
                print("Download from failed:")
