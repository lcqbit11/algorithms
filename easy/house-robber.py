#!/usr/bin/env python
# -*- coding: utf-8 -*-


def houseRobber(nums):
    """
    偷窃一个街上的屋子，数组中的每个数字表示屋子里的钱，但是如果相邻的屋子在相同的晚上都被偷窃，
    将会触发报警系统，请计算今晚在不报警的情况下能够偷窃最多多少钱
    :param nums: List[int]
    :return maxMoney: int
    """
    a = 0
    b = 0
    for i in range(len(nums)):
        temp = b
        b = max(a + nums[i], b)
        a = temp
    return b


if __name__ == "__main__":
    nums = [1,2,3,1]
    print(houseRobber(nums))