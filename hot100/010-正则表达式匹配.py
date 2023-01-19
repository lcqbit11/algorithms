#!/usr/bin/env python
# -*- coding: utf-8 -*-

##
# 给你一个字符串 s 和一个字符规律 p，请你来实现一个支持 '.' 和 '*' 的正则表达式匹配。
#
# '.' 匹配任意单个字符
# '*' 匹配零个或多个前面的那一个元素
# 所谓匹配，是要涵盖 整个 字符串 s的，而不是部分字符串。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/regular-expression-matching
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。#


# not pass
def isMatch(s, p):
    if not p:
        return not s
    first_match = True if (s and p[0] == s[0]) or (s and p[0] == '.') else False
    if len(p) >= 2 and p[1] == '*':
        return (first_match and isMatch(s[1:], p)) or isMatch(s, p[2:])
    else:
        return first_match and isMatch(s[1:], p[1:])


# can pass
# 参考链接进行理解 https://leetcode.cn/problems/regular-expression-matching/solution/dong-tai-gui-hua-zen-yao-cong-0kai-shi-si-kao-da-b/
def isMatch1(s, p):
    if not p:
        return not s

    ns = len(s) + 1
    np = len(p) + 1
    dp = [[False for _ in range(np)] for _ in range(ns)]

    dp[0][0] = True
    dp[0][1] = False
    for i in range(2, np):
        ii = i - 1
        if p[ii] == '*':
            dp[0][i] = dp[0][i - 2]

    for i in range(1, ns):
        ii = i - 1
        for j in range(1, np):
            jj = j - 1
            if s[ii] == p[jj] or p[jj] == '.':
                dp[i][j] = dp[i-1][j-1]
            elif p[jj] == '*':
                if p[jj-1] == s[ii] or p[jj-1] == '.':
                    dp[i][j] = dp[i-1][j] or dp[i][j-2]
                else:
                    dp[i][j] = dp[i][j-2]
            else:
                dp[i][j] = False

    return dp[ns-1][np-1]


if __name__ == "__main__":
    # s = "aa"
    # p = "a"
    s = "aaaaaaaaaaaaaaaaaaab"
    p = "a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*"
    print(isMatch1(s, p))
