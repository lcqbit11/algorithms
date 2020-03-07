#!/usr/bin/env python
# -*- coding: utf-8 -*-


def clockwise_p(nums):
    """
    给定一个矩阵，按照从外向里以顺时针的顺序依次打印出每个数字
    :param nums: List[List[int]]
    :return: List[int]
    """
    def once_print(nums, row_min, row_max, col_min, col_max):
        res = []
        if row_min == row_max:
            for i in range(col_min, col_max + 1):
                res.append(nums[row_min][i])
            return res
        if col_min == col_max:
            for j in range(row_min, row_max + 1):
                res.append(nums[j][col_max])
            return res

        for i in range(col_min, col_max+1):
            res.append(nums[row_min][i])
        for j in range(row_min+1, row_max+1):
            res.append(nums[j][col_max])
        for i in range(col_max-1, col_min-1, -1):
            res.append(nums[row_max][i])
        for j in range(row_max-1, row_min, -1):
            res.append(nums[j][col_min])

        return res

    m = len(nums)
    n = len(nums[0])
    res = []
    for i in range(min((m + 1) // 2, (n + 1) // 2)):
        res.extend(once_print(nums, i, m-1-i, i, n-1-i))
    return res


if __name__ == "__main__":
    nums = [[1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12],
            [13, 14, 15, 16]]
    print(clockwise_p(nums))