#!/usr/bin/env python
# -*- coding: utf-8 -*-


##
# 给你两个单词 word1 和 word2， 请返回将 word1 转换成 word2 所使用的最少操作数  。

# 你可以对一个单词进行如下三种操作：

# 插入一个字符
# 删除一个字符
# 替换一个字符

# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/edit-distance
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。#


def minDistance(word1, word2):
    if not word1 or not word2:
        return len(word1) + len(word2)
    
    m = len(word1)
    n = len(word2)
    dp = [[0] * (n+1) for _ in range(m+1)]
    for j in range(1, n+1):
        dp[0][j] = dp[0][j-1] + 1
    for i in range(1, m+1):
        dp[i][0] = dp[i-1][0] + 1
    
    for i in range(1, m+1):
        for j in range(1, n+1):
            if word1[i-1] == word2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1

    return dp[-1][-1]


word1 = "horse" 
word2 = "ros"
print(minDistance(word1, word2))
