#!/usr/bin/env python
# -*- coding: utf-8 -*-


def decode_ways(nums):
    """
    一个包含'A'-'Z'之间字母的信息，将按照下面的方式编码成数字。现在给一个非空的只包含数字的信息，请计算有多少种对应的解码后的原始信息。
    'A' -> 1
    'B' -> 2
    ...
    'Z' -> 26
    :param nums: str
    :return: int
    """
    if len(nums) == 0:
        return 0
    d = [0] * (len(nums) + 1)
    d[0] = 1  # 输入为空时，对应的解码方式的数量
    if nums[0] == "0":
        d[1] = 0
    else:
        d[1] = 1
    for i in range(1, len(nums)):
        pre = int(nums[i-1])
        cur = int(nums[i])
        number = 10 * pre + cur
        if cur != 0:
            d[i+1] += d[i]
        if pre != 0 and 0 < number <= 26:
            d[i+1] += d[i-1]
    return d[-1]


def decode_ways1(nums):
    if len(nums) == 0:
        return 0
    res_pre = 1  # 输入为空时，对应的解码方式的数量
    if nums[0] == "0":
        res = 0
    else:
        res = 1
    for i in range(1, len(nums)):
        pre = int(nums[i-1])
        cur = int(nums[i])
        number = 10 * pre + cur
        tmp = 0
        if cur != 0:
            tmp += res
        if pre != 0 and 0 < number <= 26:
            tmp += res_pre
        res_pre = res
        res = tmp
    return res


if __name__ == "__main__":
    nums = "226"
    print(decode_ways1(nums))