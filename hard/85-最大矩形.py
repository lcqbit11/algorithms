#!/usr/bin/env python
# -*- coding: utf-8 -*-


##
# 给定一个仅包含 0 和 1 、大小为 rows x cols 的二维二进制矩阵，找出只包含 1 的最大矩形，并返回其面积。#


def maximalRectangle(matrix):
    def largestRectangleArea(heights):
        if not heights:
            return 0
        
        index_arr = []
        i = 0
        heights.append(-1)
        l = len(heights)
        res = 0
        while i < l:
            if not index_arr or heights[index_arr[-1]] <= heights[i]:
                index_arr.append(i)
                i += 1
            else:
                tmp = index_arr.pop()
                width = i if not index_arr else (i - index_arr[-1] - 1)
                res = max(res, width*heights[tmp])
        return res
    
    if not matrix:
        return 0
    heights = [0] * len(matrix[0])
    rec_area = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            heights[j] = 0 if matrix[i][j] == '0' else (heights[j] + 1)
        rec_area = max(rec_area, largestRectangleArea(heights))
    
    return rec_area


matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
print(maximalRectangle(matrix))
