#!C:\python36\python3
# -*- coding: utf-8 -*-
import sys
import re
import fileinput
from subprocess import Popen, PIPE
for file_line in fileinput.input():
    # 从标准输入可以获取三个值

    # 推送前的引用指向的内容的SHA-1值，用户准备推送的内容的SHA-1值，引用的名字（分支）

    old_hash, new_hash, branch = re.split(r'\s+', file_line.strip('\n'))
    p = Popen(
        "git show --format='%%cn %%ce %%ct' --no-patch %s" % new_hash,
        shell=True,
        stdout=PIPE)
    output = p.stdout.read().decode('UTF-8')
    print(output)
# 放弃推送
print("dddfffffffffffddddffffffffssssssssssfffxzczxc")
sys.exit(1)
