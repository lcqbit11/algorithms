#!/usr/bin/env python
# -*- coding: utf-8 -*-


def cherry_pickup(grid):
    """
    https://leetcode.com/problems/cherry-pickup/
    给定一个N*N的方形网格表示樱桃区域，每个格子是0, 1, -1三个数字中一个，其中
        0：表示格子是空的，可以通行；
        1：表示格子中有一个樱桃，可以捡起樱桃然后通行；
        -1：表示格子中有刺，无法通行。
    现在需要遵循下面的规则来搜集最大数量的樱桃：
    1.从左上角（0，0）开始一直到达右下角（N-1，N-1），每次通过可通行路径0或者1，向右或者向下移动一个格子；
    2.当到达右下角（N-1，N-1）后，再每次通过可通行路径0或者1，向左或者向上移动一个格子，返回到原点左上角（0，0）处；
    3.当通过一个包含樱桃的格子后，捡起樱桃并且格子中的数值由1变为0；
    4.如果在（0，0）和（N-1，N-1）之间，没有可通行路径，那么将无法收集到樱桃。
    注意，前提是假设（0，0）和（N-1，N-1）格子中数值不等于-1。
    :param grid: List[List[int]]
    :return: int
    """
    n = len(grid)
    mx = 2 * n - 1
    dp = [[-1] * n for _ in range(n)]
    dp[0][0] = grid[0][0]
    for k in range(1, mx):
        for i in reversed(range(n)):
            for p in reversed((range(n))):
                j, q = k - i, k - p
                if j < 0 or j >= n or q < 0 or q >= n or grid[i][j] < 0 or grid[p][q] < 0:
                    dp[i][p] = -1
                    continue
                if i > 0:
                    dp[i][p] = max(dp[i][p], dp[i-1][p])
                if p > 0:
                    dp[i][p] = max(dp[i][p], dp[i][p-1])
                if i > 0 and p > 0:
                    dp[i][p] = max(dp[i][p], dp[i-1][p-1])
                if dp[i][p] >= 0:
                    dp[i][p] += grid[i][j] + (grid[p][q] if i != p else 0)

    return max(dp[n-1][n-1], 0)


if __name__ == "__main__":
    grid =[[0, 1, -1],
             [1, 0, -1],
             [1, 1, 1]]
    print(cherry_pickup(grid))