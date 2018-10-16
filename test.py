# -*- coding:utf-8 -*-
import random


def find_key(li, key):
    if li is None or len(li) < 1:
        return -1
    low = 0
    high = len(li) - 1
    while low <= high:
        mid = (low + high) // 2
        if li[mid] == key and li[mid - 1] != key:
            return mid
        elif li[mid] >= key:
            high = mid - 1
        else:
            low = mid + 1


if __name__ == '__main__':
    li = [1, 4, 7, 9, 11, 14, 14, 17]
    key = 14
    s = find_key(li, key)


class ReservoirSample(object):

    def __init__(self, size):
        self._size = size
        self._counter = 0
        self._sample = []

    def feed(self, item):
        self._counter += 1
        if len(self._sample) < self._size:
            self._sample.append(item)
            return self._sample
        rand_int = random.randint(1, self._counter)
        if rand_int <= self._size:
            self._sample[rand_int - 1] = item
        return self._sample


if __name__ == '__main__':
    rs = ReservoirSample(3)
    for item in range(1, 11):
        sample = rs.feed(item)
