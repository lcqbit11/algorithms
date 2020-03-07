#!/usr/bin/env python
# -*- coding: utf-8 -*-

def maximal_rectangle(nums):
    """
    给定一个二维矩阵，每个位置处填充着'0'或者'1'，请找出其中只包含'1'的最大矩形，并返回其最大面积
    解法参考 largest rectangle histogram，即矩阵的每一行都构成一个直方图
    :param nums: list[list[int]]
    :return: int
    """
    def largest_rectangle_histogram(heights):
        index_arr = []
        heights.append(-1)
        res = 0
        i = 0
        while i < len(heights):
            if not index_arr or heights[index_arr[-1]] <= heights[i]:
                index_arr.append(i)
                i += 1
            else:
                tmp = index_arr.pop()
                width = i if not index_arr else (i - index_arr[-1] - 1)
                res = max(res, width*heights[tmp])
        return res

    if not nums:
        return 0
    max_rec = 0
    heights = [0] * len(nums[0])
    for i in range(len(nums)):
        for j in range(len(nums[0])):
            heights[j] = 0 if nums[i][j] == '0' else (1 + heights[j])
        max_rec = max(max_rec, largest_rectangle_histogram(heights))

    return max_rec

if __name__ == "__main__":
    nums = [
              ["1","0","1","0","0"],
              ["1","0","1","1","1"],
              ["1","1","1","1","1"],
              ["1","0","0","1","0"]
           ]
    print(maximal_rectangle(nums))