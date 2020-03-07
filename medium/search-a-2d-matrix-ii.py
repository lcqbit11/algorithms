#!/usr/bin/env python
# -*- coding: utf-8 -*-


def search_a_2d_matrix_ii(matrix, target):
    """
    给定一个m*n的矩阵，请在该矩阵中找到一个目标数值，请注意，该矩阵有如下特性：
    1.每行中的整数从左到右是依次增大的
    2.每列中的整数从上到下是依次增大的
    :param matrix: List[List[int]]
    :param target: int
    :return: bool
    """
    if not matrix:
        return False
    row = len(matrix)
    col = len(matrix[0])
    i, j = row - 1, 0
    while i >= 0 and j <= col - 1:
        if matrix[i][j] < target:
            j += 1
        elif matrix[i][j] > target:
            i -= 1
        else:
            return True
    return False

    # def binary_search(nums, target):
    #     start, end = 0, len(nums)-1
    #     while start + 1 < end:
    #         mid = int((start + end) / 2)
    #         if nums[mid] < target:
    #             start = mid
    #         elif nums[mid] > target:
    #             end = mid
    #         else:
    #             return True
    #     if nums[start] == target:
    #         return True
    #     if nums[end] == target:
    #         return True
    #     return False
    #
    # for nums in matrix:
    #     if binary_search(nums, target):
    #         return True
    # return False


if __name__ == "__main__":
    nums = [
              [1,   4,  7, 11, 15],
              [2,   5,  8, 12, 19],
              [3,   6,  9, 16, 22],
              [10, 13, 14, 17, 24],
              [18, 21, 23, 26, 30]
            ]
    target = 20
    print(search_a_2d_matrix_ii(nums, target))