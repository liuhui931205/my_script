# -*- coding:utf-8 -*-
import json
import requests
from collections import namedtuple

Label = namedtuple(
        'Label', ['en_name', 'id', 'categoryId', 'color', 'name'])

with open('kd_config_v4.12.json', 'r') as f:
    data = f.read()
# data = json.load("kd_config_v4.12.json")
# # data = json.dumps(data)
# print(type(data))
# print(data)
data = json.loads(data)
print(data)
url = "http://192.168.1.132:33320/kms-sft/taskPalette/insert"
datas = {
    "version": "4.12",
    "message": data
}
headers = {'Content-Type': 'application/json'}
# datas = json.dumps(datas)
# print(datas)
json_data = requests.post(url, data=datas, headers=headers)


# kd_road_labels = {
#     Label('other', 0, 0, (64, 64, 32), u'其他'),
#     Label('ignore', 1, 1, (0, 0, 0), u'Ignore'),
#     Label('lane', 2, 2, (255, 0, 0), u'车道标线-白色'),
#     Label('left', 3, 3, (255, 192, 203), u'左侧道路边缘线'),
#     Label('right', 4, 4, (139, 0, 139), u'右侧道路边缘线'),
#     Label('v_slow', 5, 5, (32, 128, 192), u'纵向减速标线'),
#     Label('bus_lane', 6, 6, (192, 128, 255), u'专用车道标线'),
#     Label('stop', 7, 7, (255, 128, 64), u'停止线'),
#     Label('slow_let', 8, 8, (0, 255, 255), u'减速让行标线'),
#     Label('slow_zone', 9, 9, (128, 128, 255), u'减速标线/减速带'),
#     Label('sidewalk', 10, 10, (128, 192, 192), u'人行横道'),
#     Label('connection', 11, 11, (128, 128, 192), u'路面连接带'),
#     Label('stop_station', 12, 12, (240, 128, 128), u'停靠站标线'),
#     Label('in_out', 13, 13, (128, 128, 0), u'出入口标线'),
#     Label('symbol', 14, 14, (0, 0, 255), u'文字符号类'),
#     Label('fish_lane', 15, 15, (0, 255, 0), u'导流线（鱼刺线）'),
#     Label('stop_gird', 16, 16, (255, 255, 0), u'停止网格标线'),
#     Label('distance', 17, 17, (255, 128, 255), u'车距确认线'),
#     Label('road', 18, 18, (192, 192, 192), u'道路'),
#     Label('objects', 19, 19, (128, 0, 0), u'车辆及路面上其他物体'),
#     Label('curb', 20, 20, (0, 139, 139), u'虚拟车道线-路缘石'),
#     Label('fence', 21, 21, (255, 106, 106), u'虚拟车道线-防护栏'),
#     Label('virtual', 22, 22, (118, 180, 254), u'虚拟车道线-其他'),
#     Label('tide_lane', 23, 23, (75, 0, 130), u'潮汐车道线'),
#     Label('left_wait', 24, 24, (144, 238, 144), u'左弯待转区线'),
#     Label('guide_lane', 25, 25, (0, 255, 127), u'可变导向车道线'),
#     Label('lane_y', 26, 26, (255, 165, 0), u'车道标线-黄色'),
#     Label('hump', 27, 27, (72, 61, 139), u'减速丘'),
#     Label('warning', 28, 28, (255, 0, 255), u'警告标示牌'),
#     Label('prohibition', 29, 29, (220, 20, 60), u'禁令标志牌'),
#     Label('instructive', 30, 30, (255, 215, 0), u'指示标志牌'),
#     Label('highway', 31, 31, (0, 0, 128), u'高速公路指路标志牌'),
#     Label('directing', 32, 32, (153, 102, 51), u'普通道路指路标志牌'),
#     Label('tourist', 33, 33, (102, 102, 0), u'旅游区标志牌'),
#     Label('assist', 34, 34, (0, 255, 102), u'辅助标志牌'),
#     Label('task', 35, 35, (0, 102, 0), u'作业区标志牌'),
#     Label('other', 36, 36, (204, 255, 0), u'其他交通标志牌'),
#     Label('pole', 37, 37, (255, 140, 0), u'杆'),
#     Label('sky', 38, 38, (135, 206, 235), u'天空'),
#     Label('curbs', 39, 39, (127, 255, 0), u'路缘石'),
#     Label('barrier', 40, 40, (0, 250, 154), u'凸型屏障'),
#     Label('fences', 41, 41, (5, 107, 47), u'防护栏'),
#     Label('light', 42, 42, (255, 69, 0), u'灯'),
#     Label('cover', 43, 43, (178, 34, 34), u'井盖'),
#     Label('fence', 44, 44, (65, 105, 225), u'可移动栅栏'),
#     Label('reflector', 45, 45, (50, 205, 50), u'反光标'),
#     Label('old_line', 46, 46, (255, 20, 147), u'旧车道线'),
#     Label('w_dot_line', 47, 47, (127, 255, 212), u'车道标线-白虚线'),
#     Label('y_dot_line', 48, 48, (199, 21, 133), u'车道标线-黄虚线'),
# }