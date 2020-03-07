#!/usr/bin/env python
# -*- coding: utf-8 -*-


def max_sum_subset(numbers):
    """
    计算以数组中每个元素结尾的连续子集的最大和
    动态规划的思路就是求解以当前元素结尾的子数组的最大和
    :param numbers: List[int]
    :return: int
    """
    sum_subset = -float("inf")
    max_result = -float("inf")
    for i in range(len(numbers)):
        if sum_subset <= 0:
            sum_subset = numbers[i]
        else:
            sum_subset += numbers[i]
        if max_result < sum_subset:
            max_result = sum_subset
    return max_result


if __name__ == "__main__":
    numbers = [1, -2, 3, 10, -4, 7, 2, -5]
    print(max_sum_subset(numbers))