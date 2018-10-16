#!/usr/bin/env python
# encoding=utf-8

"""移除已标注的数据，并抽取指定数量数据"""
import os
import random
import shutil
import json

# src_dir = '/data/deeplearning/chenhuizhen/wangjing/chengdu.autosele.res/sele'
# src_dir = '/data/deeplearning/chenhuizhen/wangjing/chengdu50000.autosele.v2/sele'
# srclistfile_list = '/data/deeplearning/chenhuizhen/wangjing/file/ningbov1_1.list'
# src_dir = '/data/deeplearning/chenhuizhen/wangjing/liuhuisele/fish_outin.select/fish'
# src_dir = '/data/deeplearning/chenhuizhen/wangjing/germanyselev2'
src_dir = '/data/deeplearning/train_platform/select_data/out_image/wuhan/wuhan.sele/sele'
# f = open(srclistfile_list,'r')
# src_file_list = []
# for line in f :
#     line = line[:-1]
#     src_file_list.append(line)
src_file_list = []
for image_file in os.listdir(src_dir):
    if image_file.endswith('jpg'):
        src_file_list.append(image_file)

# rm_dir = '/data/deeplearning/chenhuizhen/out_suzhou'
# rm_file_list = []
# for image_file in os.listdir(rm_dir):
#     if image_file.endswith('jpg'):
#         rm_file_list.append(image_file)

rmlistfile_list = '/data/deeplearning/train_platform/select_data/labeled.list/wuhan1000.v1.list'
f = open(rmlistfile_list, 'r')
rm_file_list = []
for line in f:
    line = line[:-1]
    rm_file_list.append(line)

# shanghaiv2.2000.list

rmlistfile_list2 = '/data/deeplearning/train_platform/select_data/labeled.list/wuhan1000.v2.list'
f = open(rmlistfile_list2, 'r')
rm_file_list2 = []
for line in f:
    line = line[:-1]
    rm_file_list2.append(line)
#
rmlistfile_list3 = '/data/deeplearning/train_platform/select_data/labeled.list/wuhan1000.sele.v1.list'
f = open(rmlistfile_list3, 'r')
rm_file_list3 = []
for line in f:
    line = line[:-1]
    rm_file_list3.append(line)
# # # #
rmlistfile_list4 = '/data/deeplearning/train_platform/select_data/labeled.list/wuhan1000.sele.v2.list'
f = open(rmlistfile_list4, 'r')
rm_file_list4 = []
for line in f:
    line = line[:-1]
    rm_file_list4.append(line)
# #
rmlistfile_list5 = '/data/deeplearning/train_platform/select_data/labeled.list/wuhan1000.sele.v3.list'
f = open(rmlistfile_list5,'r')
rm_file_list5 = []
for line in f :
    line = line[:-1]
    rm_file_list5.append(line)

# rmlistfile_list6 = '/data/deeplearning/chenhuizhen/wangjing/file/germanyv6.list'
# f = open(rmlistfile_list6,'r')
# rm_file_list6 = []
# for line in f :
#     line = line[:-1]
#     rm_file_list6.append(line)
#
# rmlistfile_list7 = '/data/deeplearning/chenhuizhen/wangjing/file/germany.selev1.list'
# f = open(rmlistfile_list7,'r')
# rm_file_list7= []
# for line in f :
#     line = line[:-1]
#     rm_file_list7.append(line)
#
# rmlistfile_list8 = '/data/deeplearning/chenhuizhen/wangjing/file/germany.selev2.list'
# f = open(rmlistfile_list8,'r')
# rm_file_list8= []
# for line in f :
#     line = line[:-1]
#     rm_file_list8.append(line)
#
# rmlistfile_list9 = '/data/deeplearning/chenhuizhen/wangjing/file/germany.fish.list'
# f = open(rmlistfile_list9,'r')
# rm_file_list9= []
# for line in f :
#     line = line[:-1]
#     rm_file_list9.append(line)
#
# rmlistfile_list10 = '/data/deeplearning/chenhuizhen/wangjing/file/germany.out_in.list'
# f = open(rmlistfile_list10,'r')
# rm_file_list10= []
# for line in f :
#     line = line[:-1]
#     rm_file_list10.append(line)
#
# #germany.selev3.list
#
# rmlistfile_list11 = '/data/deeplearning/chenhuizhen/wangjing/file/germany.selev3.list'
# f = open(rmlistfile_list11,'r')
# rm_file_list11= []
# for line in f :
#     line = line[:-1]
#     rm_file_list11.append(line)

# inter_list = list(set(rm_file_list).intersection(set(src_file_list)))#
# inter_list = list(set(rm_file_list).intersection(set(rm_file_list2)))#

unin_list = list(set(rm_file_list).union(set(rm_file_list2)))
unin_list = list(set(unin_list).union(set(rm_file_list3)))
unin_list = list(set(unin_list).union(set(rm_file_list4)))
unin_list = list(set(unin_list).union(set(rm_file_list5)))
# unin_list = list(set(unin_list).union(set(rm_file_list6)))
# unin_list = list(set(unin_list).union(set(rm_file_list7)))
# unin_list = list(set(unin_list).union(set(rm_file_list8)))
# unin_list = list(set(unin_list).union(set(rm_file_list9)))
# unin_list = list(set(unin_list).union(set(rm_file_list10)))
# unin_list = list(set(unin_list).union(set(rm_file_list11)))
print("len(unin_list)--{}".format(len(unin_list)))

sam_num = 1000
# goal_list = list(set(src_file_list).difference(set(rm_file_list))) #remove one list
# goal_list = list(set(src_file_list).difference(set(unin_list))) #remove  two list
goal_list = list(set(src_file_list).difference(set(unin_list)))  # remove  three list

print("len(src_file_list)--{}----len(goal_list)--{}".format(len(src_file_list), len(goal_list)))

random.shuffle(goal_list)
sam_list = goal_list[:sam_num]
print('sam_list--{}'.format(len(sam_list)))

out_dir = '/data/deeplearning/train_platform/select_data/out_image/wuhan/wuhan1000.sele.v4'
if not os.path.exists(out_dir):
    os.makedirs(out_dir)

json_data = []
for chosen_id in sam_list:
    chosen_id = chosen_id[:-11]
    json_data.append({
        "trackPointId": chosen_id
    })

with open(os.path.join(out_dir, "task_list.json"), "w") as f:
    json.dump(json_data, f)

for img_file in sam_list:
    shutil.copy(os.path.join(src_dir, img_file), os.path.join(out_dir, img_file))
print('save_file-----{}'.format(out_dir))
