import os
import json


def create(src, dest, imgoprange, roadelement, source, author, annotype, city, datakind):
    lists = []
    task_name = os.path.basename(src)
    dest_path = os.path.join(dest, task_name)
    if not os.path.exists(dest_path):
        os.makedirs(dest_path)
    s = os.listdir(src)
    for i in s:
        image_path = os.path.join(src, i)
        img_li = os.listdir(image_path)
        for j in img_li:
            if j.startswith('label-') and j.endswith('.png'):
                trackpointid = j[6:-11]
                dicts = {}
                dicts["TRACKPOINTID"] = trackpointid
                dicts["IMGOPRANGE"] = imgoprange
                dicts["ROADELEMENT"] = roadelement
                dicts["SOURCE"] = source
                dicts["AUTHOR"] = author
                dicts["CITY"] = city
                dicts["DATAKIND"] = datakind
                dicts["ANNOTYPE"] = annotype
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
                open(os.path.join(dest_path, j), "wb").write(open(os.path.join(src, i, j), "rb").read())
                lists.append(dicts)
    json.dump(lists, open(os.path.join(dest_path, 's.json'), 'w'))


if __name__ == '__main__':
    src = 'F:\mywork\script\\test11'
    dest = 'F:\mywork'
    imgoprange = 'ss'
    roadelement = 'sd'
    source = 'sd'
    author = 'sd'
    annotype = 'sd'
    city = 'sd'
    datakind = 'sad'
    create(src, dest, imgoprange, roadelement, source, author, annotype, city, datakind)
