#!/usr/bin/env python
# -*- coding: utf-8 -*-


def edit_distance(word1, word2):
    """
    给定两个单词word1和word2，请找出将word1转化成word2所需要最少的步骤数量。
    注意，在单词上有三种操作：
    1.插入一个字母；
    2.删除一个字母；
    3替换一个字母。
    解答参考：https://blog.csdn.net/chichoxian/article/details/53944188
    :param word1: str
    :param word2: str
    :return: int
    """
    m, n = len(word1) + 1, len(word2) + 1
    dp = [[0] * n for _ in range(m)]
    dp[0][0] = 0
    for i in range(1, m):
        dp[i][0] = dp[i - 1][0] + 1
    for i in range(1, n):
        dp[0][i] = dp[0][i - 1] + 1

    tmp = 0
    for i in range(1, m):
        for j in range(1, n):
            if word1[i - 1] == word2[j - 1]:
                tmp = 0
            else:
                tmp = 1
            dp[i][j] = min(dp[i - 1][j] + 1, dp[i][j - 1] + 1, dp[i - 1][j - 1] + tmp)

    return dp[m - 1][n - 1]


if __name__ == "__main__":
    word1 = "horse"
    word2 = "ros"
    print(edit_distance(word1, word2))