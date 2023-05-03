#!/usr/bin/env python
# -*- coding: utf-8 -*-


##
# 给定一个包含非负整数的 m x n 网格 grid ，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。

# 说明：每次只能向下或者向右移动一步。#


def minPathSum(grid):
    if not grid:
        return 0
    
    m = len(grid)
    n = len(grid[0])
    dp = [0] * n
    dp[0] = grid[0][0]
    for i in range(1, n):
        dp[i] = dp[i-1] + grid[0][i]
    
    for i in range(1, m):
        for j in range(n):
            if j == 0:
                dp[j] = dp[j] + grid[i][j]
            else:
                dp[j] = min(dp[j-1], dp[j]) + grid[i][j]
    
    return dp[-1]


grid = [[1,3,1],[1,5,1],[4,2,1]]
print(minPathSum(grid))
