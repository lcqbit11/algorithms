#!/usr/bin/env python
# -*- coding: utf-8 -*-


def trapping_rain_water(height):
    """
    给定n个表示海拔高度的非负整数，其中每个块的宽度为1，请计算下雨后它能承载多少水
    :param nums: List[int]
    :return: int
    """
    height_max = 0
    index_max = 0
    # 找到高度最高的位置下标和对应的高度
    for i in range(len(height)):
        if height_max < height[i]:
            height_max = height[i]
            index_max = i

    pre_area = 0
    pre_height = 0
    for i in range(0, index_max):
        if pre_height < height[i]:
            pre_height = height[i]
        pre_area += pre_height - height[i]
    after_area = 0
    after_height = 0
    # for i in reversed(range(index_max + 1, len(height))):
    for i in range(len(height) - 1, index_max, -1):
        if after_height < height[i]:
            after_height = height[i]
        after_area += after_height - height[i]

    return pre_area + after_area


if __name__ == "__main__":
    nums = [0,1,0,2,1,0,1,3,2,1,2,1]
    print(trapping_rain_water(nums))