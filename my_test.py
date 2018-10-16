import os
import base64

with open("./test.txt", "r") as f:
    data = f.readlines()

if isshuffle:
    random.seed(1000)
    random.shuffle(data)
if ratio > 1.0:
    sel_count = int(ratio)
else:
    sel_count = int(ratio * total_count)
sel_points = data[:sel_count]
json_data = []
for i in sel_points:
    li = i.split(',')
    imgdata = base64.b64decode(li[3].strip())

    dicts = {}
    dicts["TRACKPOINTID"] = li[0].strip()
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
    dicts["TRACKID"] = li[0].strip()
    dicts["handle"] = ""
    json_data.append(dicts)
    image_name = "{}_00_004.jpg".format(li[0].strip())
    path =
    file = open('1.jpg', 'wb')
    with open('')
with open(os.path.join(output_dir, "task_list.json"), "w") as f:
    json.dump(json_data, f)