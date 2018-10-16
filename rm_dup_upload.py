# -*- coding:utf-8 -*-
import json
import os
import re
import random
import requests
import shutil


def copyFiles(sourceDir, targetDir):
    for f in os.listdir(sourceDir):
        sourceF = os.path.join(sourceDir, f)
        targetF = os.path.join(targetDir, f)
        if os.path.isfile(sourceF):
            # 创建目录
            if not os.path.exists(targetDir):
                os.makedirs(targetDir)
                # 文件不存在，或者存在但是大小不同，覆盖
            if not os.path.exists(targetF) or (
                    os.path.exists(targetF) and (os.path.getsize(targetF) != os.path.getsize(sourceF))):
                open(targetF, "wb").write(open(sourceF, "rb").read())
            else:
                pass
        elif os.path.isdir(sourceF):
            if not os.path.exists(targetF):
                os.makedirs(targetF)
            copyFiles(sourceF, targetF)


def rm_dup_upload(output_dir):
    krs = "http://10.11.5.74:13100/krs/"
    dest_dir = "/data/deeplearning/auto_sele_datas"
    task = os.path.basename(os.path.dirname(output_dir))
    name = os.path.basename(output_dir)
    s_name = name.split('.')[0]
    src_dir = os.path.join(output_dir, 'sele')
    src_file_list = []
    for image_file in os.listdir(src_dir):
        if image_file.endswith('jpg'):
            src_file_list.append(image_file)

    for v in range(1, 5):
        rmlistfile = []
        task_path = os.path.dirname(output_dir)
        path_li = os.listdir(task_path)
        name_li = []
        for i in path_li:
            if re.match(r'.*v\d+', i):
                name_li.append(os.path.join(task_path, i))
        if name_li:
            for i in name_li:
                li = os.listdir(i)
                for j in li:
                    if j.endswith('.jpg'):
                        rmlistfile.append(j)
        goal_list = list(set(src_file_list).difference(set(rmlistfile)))
        random.shuffle(goal_list)
        sam_list = goal_list[:1000]
        p_name = s_name + str(1000) + ".sele.v" + str(v)
        out_dir = os.path.join(task_path, p_name)
        if not os.path.exists(out_dir):
            os.makedirs(out_dir)

        json_data = []
        for chosen_id in sam_list:
            chosen_id = chosen_id[:-11]
            url = krs + 'track/point/get?trackPointId={}'.format(chosen_id)
            req_data = requests.get(url)
            req_data = json.loads(req_data.text)
            trackid = req_data['result']['trackId']
            dicts = {}
            dicts["TRACKPOINTID"] = chosen_id
            dicts["IMGOPRANGE"] = ""
            dicts["ROADELEMENT"] = ""
            dicts["SOURCE"] = ""
            dicts["AUTHOR"] = ""
            dicts["CITY"] = ""
            dicts["DATAKIND"] = ""
            dicts["ANNOTYPE"] = ""
            dicts["PACKAGEID"] = ""
            dicts["ROADANGLE"] = ""
            dicts["ISREPAIR"] = ""
            dicts["DOWNSUFFIX"] = ""
            dicts["TRACKPOINTSEQ"] = ""
            dicts["TRACKLOCATION"] = ""
            dicts["IMGID"] = ""
            dicts["DOWNTYPE"] = ""
            dicts["BATCH"] = ""
            dicts["SCENE"] = ""
            dicts["EXTEND2"] = ""
            dicts["EXTEND3"] = ""
            dicts["MARKTYPE"] = ""
            dicts["EXTEND4"] = ""
            dicts["WEATHER"] = ""
            dicts["ROADTYPE"] = ""
            dicts["ERRORTYPE"] = ""
            dicts["TRACKID"] = ""
            dicts["EXTEND1"] = ""
            dicts["TASKID"] = ""
            dicts["MARKTASKID"] = ""
            dicts["DATATYPE"] = ""
            dicts["DOWNSEQ"] = ""
            dicts["MARKBY"] = ""
            dicts["SEQ"] = ""
            dicts["MARKTIME"] = ""
            dicts["TRACKID"] = trackid
            dicts["handle"] = ""
            json_data.append(dicts)
        with open(os.path.join(out_dir, "task_list.json"), "w") as f:
            json.dump(json_data, f)

        for img_file in sam_list:
            shutil.copy(os.path.join(src_dir, img_file), os.path.join(out_dir, img_file))

        pa = os.path.basename(out_dir)
        files = os.listdir(dest_dir)
        dests = os.path.join(dest_dir, task, pa)
        if task not in files:
            os.makedirs(dests)
        copyFiles(out_dir, dests)


if __name__ == '__main__':
    rm_dup_upload("/data/deeplearning/train_platform/select_data/out_image/dalian/dalian.sele")
