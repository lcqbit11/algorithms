#!/usr/bin/env python
# -*- coding: utf-8 -*-


def smaller_num(nums):
    if not nums:
        return
    l = len(nums)
    res = [0] * l
    for i in range(l):
        count = 0
        for j in range(l):
            if i != j and nums[i] > nums[j]:
                count += 1
        res[i] = count
    return res


if __name__ == "__main__":
    nums = [6,5,4,8]
    print(smaller_num(nums))
                