#!/usr/bin/env python
# -*- coding: utf-8 -*-

##
# 给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。
# 求在该柱状图中，能够勾勒出来的矩形的最大面积。#


def largestRectangleArea(heights):
    if not heights:
        return 0
    
    res = 0
    heights.append(-1)
    index_list = []
    cur = 0
    while cur < len(heights):
        if not index_list or heights[index_list[-1]] <= heights[cur]:
            index_list.append(cur)
            cur += 1
        else:
            tmp = index_list.pop()
            width = cur if not index_list else (cur-index_list[-1]-1)
            res = max(res, width*heights[tmp])
    
    return res


heights = [2,1,5,6,2,3]
print(largestRectangleArea(heights))
