#!/usr/bin/env python
# -*- coding: utf-8 -*-


def sortByBits(arr):
    def partition(mp, low, high):
        for i in range(low, high):
            for j in range(low, high-(i-low)):
                if arr[mp[j][0]] > arr[mp[j+1][0]]:
                    mp[j], mp[j+1] = mp[j+1], mp[j]

    if not arr:
        return
    m = {}
    l = len(arr)
    for i in range(l):
        tmp = arr[i]
        mask = 1
        m[i] = 0
        while tmp > 0:
            if tmp & mask:
                m[i] += 1
            tmp = tmp >> 1
    m = sorted(m.items(), key=lambda x: x[1])
    start = end = 0
    for i in range(1, l):
        if m[i][1] == m[i-1][1]:
            end += 1
        if m[i][1] != m[i-1][1] or i == l-1:
            partition(m, start, end)
            end += 1
            start = end
    res = [arr[m[i][0]] for i in range(l)]
    return res
        

if __name__ == "__main__":
    arr = [2,3,5,7,11,13,17,19]
    res = sortByBits(arr)
    print(res)