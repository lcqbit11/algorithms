#!/usr/bin/env python
# -*- coding: utf-8 -*-


def sort_colors(nums):
    """
    给定一个n个元素的数组，包含红、白、蓝三种颜色的物体，对他们进行就地排序后，使得相同颜色的物体相邻，
    并且按照红、白、蓝的颜色顺序进行排序。这里，我们使用整数0、1、2分别表示红、白、蓝三种颜色。
    :param nums: List[int]
    :return: List[int]
    """
    if len(nums) <= 1:
        return nums
    for i in range(0, len(nums)-1):
        for j in range(1, len(nums)-i):
            if nums[j] < nums[j-1]:
                tmp = nums[j]
                nums[j] = nums[j-1]
                nums[j-1] = tmp
    return nums


def sort_colors1(nums):
    red_count = white_count = blue_count = 0
    for i in range(len(nums)):
        if nums[i] == 0:
            red_count += 1
        elif nums[i] == 1:
            white_count += 1
        else:
            blue_count += 1
    for i in range(len(nums)):
        if i+1 <= red_count:
            nums[i] = 0
        elif i+1 <= red_count+white_count:
            nums[i] = 1
        else:
            nums[i] = 2
    return nums


def sort_colors2(nums):
    if len(nums) <= 1:
        return nums
    red, blue = 0, len(nums) - 1
    i = 0
    while i <= blue:
        if nums[i] == 0:
            tmp = nums[i]
            nums[i] = nums[red]
            nums[red] = tmp
            red += 1
        elif nums[i] == 2:
            tmp = nums[i]
            nums[i] = nums[blue]
            nums[blue] = tmp
            blue -= 1
            i -= 1
        i += 1
    return nums


if __name__ == "__main__":
    # nums = [2,0,2,1,1,0]
    nums = [2, 2]
    print(sort_colors2(nums))