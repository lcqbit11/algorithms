#!/usr/bin/env python
# -*- coding: utf-8 -*-


def minimum_path_sum(grid):
    """
    给定一个m*n的矩阵，每个位置的元素都为非负数，请找到一条从左上方到右下方的路径，使得该路径所经过位置的元素之和最小。
    在任何位置只能向下或者向右移动。
    :param grid: List[List[int]]
    :return: int
    """
    # def recursive_path(grid, row, col):
    #     if row == 1:
    #         return sum(grid[0][:col])
    #     elif col == 1:
    #         return sum([grid[i][0] for i in range(row)])
    #     else:
    #         return min(recursive_path(grid, row-1, col), recursive_path(grid, row, col-1)) + grid[row-1][col-1]

    if not grid:
        return 0
    m = len(grid)
    n = len(grid[0])
    # dp_path = [sum(grid[0][:i+1]) for i in range(n)]
    dp_path = [0] * n
    dp_path[0] = grid[0][0]
    for i in range(1, n):
        dp_path[i] = dp_path[i-1] + grid[0][i]
    for i in range(1, m):
        for j in range(n):
            if j == 0:
                dp_path[j] = dp_path[j] + grid[i][0]
            else:
                dp_path[j] = min(dp_path[j], dp_path[j-1]) + grid[i][j]
    return dp_path[n-1]

    # if not grid:
    #     return 0
    # m = len(grid)
    # n = len(grid[0])
    # dp_path = [[0] * n for _ in range(m)]
    # dp_path[0][0] = grid[0][0]
    # for i in range(1, n):
    #     dp_path[0][i] = dp_path[0][i-1] + grid[0][i]
    # for i in range(1, m):
    #     dp_path[i][0] = dp_path[i-1][0] + grid[i][0]
    # for i in range(1, m):
    #     for j in range(1, n):
    #         dp_path[i][j] = min(dp_path[i][j-1], dp_path[i-1][j]) + grid[i][j]
    # return dp_path[m-1][n-1]


    # dp_path = [[0] * n for _ in range(m)]
    # for i in range(m):
    #     dp_path[i][0] = sum([grid[j][0] for j in range(i+1)])
    # for i in range(n):
    #     dp_path[0][i] = sum(grid[0][:i+1])
    # for i in range(1, m):
    #     for j in range(1, n):
    #         dp_path[i][j] = min(dp_path[i][j-1], dp_path[i-1][j]) + grid[i][j]
    # return dp_path[m-1][n-1]


    # return recursive_path(grid, m, n)


if __name__ == "__main__":
    grid = [
              [1,3,1],
              [1,5,1],
              [4,2,1]
            ]

    print(minimum_path_sum(grid))

