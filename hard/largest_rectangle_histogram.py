#!/usr/bin/env python
# -*- coding: utf-8 -*-


def largest_rectangle_histogram(nums):
    """
    一个只包含非负数值的数组，每个元素表示直方图中的对应的高度，每个元素对应的宽度均为1
    计算直方图中构成的矩形面积的最大值
    :param nums: List
    :return: int
    """
    res = 0
    nums.append(0)
    cur = 0
    asc_indexs = []
    while cur < len(nums):
        if len(asc_indexs) == 0 or nums[asc_indexs[-1]] <= nums[cur]:
            asc_indexs.append(cur)
            cur += 1
        else:
            index = asc_indexs.pop()
            width = cur if not asc_indexs else cur-asc_indexs[-1]-1
            res = max(res, nums[index]*width)
    return res


if __name__ == "__main__":
    nums = [2,1,5,6,2,3]
    print(largest_rectangle_histogram(nums))