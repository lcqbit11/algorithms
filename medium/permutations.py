#!/usr/bin/env python
# -*- coding: utf-8 -*-


def permutations(nums):
    """
    给定一个包含不同整数的数组，返回数组的全排列的各个数组
    :param nums: List[int]
    :return: List[List[int]]
    """
    def fun(nums_fun, path, res):
        if not nums_fun:
            return res.append(path)
        for i in range(0, len(nums_fun)):
            fun(nums_fun[:i] + nums_fun[i+1:], path + [nums_fun[i]], res)

    # add on 2019/11/06.
    def fun1(nums_fun1, insert_res):
        if len(nums_fun1) == 0:
            res.append(insert_res)
        else:
            for j in range(0, len(insert_res) + 1):
                fun1(nums_fun1[1:] if len(nums_fun1) > 1 else [], insert_res[:j] + [nums_fun1[0]] + insert_res[j:])

    res = []
    fun(nums, [], res)
    # fun1(nums, [])
    return res


if __name__ == "__main__":
    nums = [1, 2, 3]
    print(permutations(nums))