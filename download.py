# -*- coding:utf-8 -*-
import json
import os
import requests
import cv2
import numpy as np
import multiprocessing


def download_or(url_li):
    err = []
    for url, name in url_li.items():

        res_data = requests.post(url=url)
        content_type = res_data.headers['Content-Type']
        if str(content_type).startswith("image"):
            err.append(name)
            continue
        origin_image_data = res_data.content
        _image0 = np.asarray(bytearray(origin_image_data), dtype="uint8")
        origin_image = cv2.imdecode(_image0, cv2.IMREAD_COLOR)
        img_array = cv2.imencode('.jpg', origin_image)
        img_data = img_array[1]
        image_data = img_data.tostring()

        with open('./origin_image/' + name + '_70_000.jpg', "wb") as f:
            f.write(image_data)

    fl = open('./origin_image/error.txt', 'a')
    for i in err:
        fl.write(i + '\n')
    fl.close()


def download_la(url_li):
    err = []
    for url, name in url_li.items():
        url1 = url.split('?')[0]
        url = url1 + '?trackPointId=' + name + '&type=70&seq=001&imageType=png'
        res_data = requests.post(url=url)
        content_type = res_data.headers['Content-Type']
        if not str(content_type).startswith("image"):
            err.append(name)
            continue
        label_image_data = res_data.content
        _image0 = np.asarray(bytearray(label_image_data), dtype="uint8")
        label_image_data = cv2.imdecode(_image0, cv2.IMREAD_COLOR)
        img_array = cv2.imencode('.png', label_image_data)
        img_data = img_array[1]
        image_data = img_data.tostring()
        with open('./label_image/' + name + '_70_001.png', "wb") as f:
            f.write(image_data)
    fl = open('./label_image/error.txt', 'a')
    for i in err:
        fl.write(i + '\n')
    fl.close()


if __name__ == '__main__':
    url_li = {}
    if not os.path.exists('origin_image'):
        os.mkdir('origin_image')
    if not os.path.exists('label_image'):
        os.mkdir('label_image')

    with open("1.txt", "r", encoding="utf-8") as f:
        json_params = json.load(f)

        if json_params["code"] == "0" and json_params["result"] != '':
            for k, v in json_params["result"].items():
                for dic in json_params["result"][k]:
                    if dic["name"] == "TRACKPOINTID":
                        url_li[k] = dic["value"]
    pro_or = multiprocessing.Process(target=download_or, args=(url_li,))
    pro_la = multiprocessing.Process(target=download_la, args=(url_li,))
    pro_or.start()
    pro_la.start()

