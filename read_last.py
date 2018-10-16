# -*- coding:utf-8 -*-
import linecache

filename = './kddata_cls15_beijing.train.log.20180801'


# 放入缓存防止内存过载
def get_line_count(filename):
    line_count = 0
    file = open(filename, 'r+')
    while True:
        buffer = file.read(8192 * 1024)
        if not buffer:
            break
        line_count += buffer.count('\n')
    file.close()
    return line_count


if __name__ == '__main__':
    n = 1000  # get the last 30 lines
    linecache.clearcache()
    line_count = get_line_count(filename)
    line_count = line_count - n
    for i in range(n + 1):  # the last 30 lines
        last_line = linecache.getline(filename, line_count)
        line_count += 1
