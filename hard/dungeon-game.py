#!/usr/bin/env python
# -*- coding: utf-8 -*-

def dungeon_game(dungeon):
    """
    https://leetcode.com/problems/dungeon-game/
    给定一个二维网格，国王在左上角，公主在右下角，为了最快能够救得公主，国王决定往右走或者往下走，
    格子里面的数字，如果是负值，表示有恶魔，经过则会损失掉格子数值大小的血量，
    如果是正值，表示有魔法棒，经过则会加相应数值大小的血量，如果是0值的话，经过后血量则没有变化
    :param dungeon: List[List[int]]
    :return: int
    """
    n = len(dungeon)
    m = len(dungeon[0])
    dp = [[float('inf')] * (m + 1) for _ in range(len(dungeon)+1)]
    dp[n][m-1] = dp[n-1][m] = 1
    for i in reversed(range(0, n)):
        for j in reversed(range(0, m)):
            dp[i][j] = max(1, min(dp[i+1][j], dp[i][j+1]) - dungeon[i][j])

    return dp[0][0]


def dungeon_game1(dungeon):
    n = len(dungeon)
    m = len(dungeon[0])
    dp = [float('inf')] * (m+1)
    dp[m-1] = 1
    for i in reversed(range(0, n)):
        for j in reversed(range(0, m)):
            dp[j] = max(1, min(dp[j], dp[j+1]) - dungeon[i][j])

    return dp[0]


if __name__ == "__main__":
    dungeon = [[-2, -3, 3],
               [-5, -10, 1],
               [10, 30, -5]
               ]
    print(dungeon_game1(dungeon))
