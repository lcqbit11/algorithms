#!/usr/bin/rnv python
# -*- coding: utf-8 -*-


def maximal_square(nums):
    """
    给定一个矩形框，每个位置上为'0'或者'1'，请找出包含的元素全部为1的最大的正方形框，并计算其面积
    :param nums: List[List[str]]
    :return: int
    """
    if not nums:
        return 0
    n = len(nums)
    m = len(nums[0])
    dp = [[0] * m for _ in range(n)]
    for i in range(m):
        dp[0][i] = int(nums[0][i])
    for i in range(n):
        dp[i][0] = int(nums[i][0])
    for i in range(1, n):
        for j in range(1, m):
            if int(nums[i][j]) == 1:
                dp[i][j] = min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1]) + 1
    return max(map(max, dp)) ** 2


if __name__ == "__main__":
    nums = [["1","0","1","0","0"],
            ["1","0","1","1","1"],
            ["1","1","1","1","1"],
            ["1","0","0","1","0"]]
    print(maximal_square(nums))