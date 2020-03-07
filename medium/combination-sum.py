#!/usr/bin/env python
# -*- coding: utf-8 -*-


def combination_sum(nums, target):
    """
    给定一个不包含重复数值的候选数字集candidates和一个目标数值target，请找到候选子集数字加和等于目标数值的所有组合。
    注意：candidates中的每个数字可以重复使用无限次。
    :param nums: List[int]
    :param target: int
    :return: List[List[int]]
    """
    def sub_set_sum(nums, target, start, path, res):
        if target == 0:
            return res.append(path+[])
        for i in range(start, len(nums)):
            if target - nums[i] >= 0:
                path.append(nums[i])
                sub_set_sum(nums, target - nums[i], i, path, res)
                path.pop()

    res = []
    sub_set_sum(nums, target, 0, [], res)
    return res


def combination_sum1(candidates, target):
    d = {}
    for candidate in candidates:
        for i in range(candidate, target + 1):
            if i == candidate:
                if i not in d:
                    d[i] = [[candidate]]
                else:
                    d[i].append([candidate])
            elif i - candidate in d:
                for num_set in d[i - candidate]:
                    tmp = num_set + [candidate]
                    if i not in d:
                        d[i] = [tmp]
                    else:
                        d[i].append(tmp)
    if target in d:
        return d[target]
    else:
        return []


if __name__ == "__main__":
    nums = [2,3,5]
    target = 8
    print(combination_sum(nums, target))