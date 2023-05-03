#!/usr/bin/env python
# -*- coding: utf-8 -*-


##
# 给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
# 
# #


from inspect import trace


def trap(height):
    if not height:
        return 0
    
    height_max = 0
    height_index = 0
    for i in range(len(height)):
        if height_max < height[i]:
            height_max = height[i]
            height_index = i
    
    pre_height = 0
    pre_area = 0
    for i in range(0, height_index):
        if pre_height < height[i]:
            pre_height = height[i]
        pre_area += pre_height - height[i]
    
    after_height = 0
    after_area = 0
    for i in reversed(range(height_index + 1, len(height))):
        if after_height < height[i]:
            after_height = height[i]
        after_area += after_height - height[i]
    
    return pre_area + after_area


height = [0,1,0,2,1,0,1,3,2,1,2,1]
print(trap(height))
