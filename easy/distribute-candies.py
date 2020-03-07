#!/usr/bin/env python
# -*- coding: utf-8 -*-


def distributeCandies(nums):
    """
    数组长度为偶数，数组中不同的数字表示糖果的不同类别，需要按照数量将糖果平均
    分给弟弟和妹妹，如何分配可以使妹妹获得最多种类的糖果
    :param nums:
    :return: number
    """
    return min(len(nums)/2, len(set(nums)))


if __name__ == "__main__":
    nums = [1,1,2,3]
    print(distributeCandies(nums))