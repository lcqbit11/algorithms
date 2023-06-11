#!/usr/bin/env python
# -*- coding: utf-8 -*-

##
# 给你一个只包含 '(' 和 ')' 的字符串，找出最长有效（格式正确且连续）括号子串的长度。
#
#  
#
# 示例 1：
#
# 输入：s = "(()"
# 输出：2
# 解释：最长有效括号子串是 "()"
# 示例 2：
#
# 输入：s = ")()())"
# 输出：4
# 解释：最长有效括号子串是 "()()"
# 示例 3：
#
# 输入：s = ""
# 输出：0
#  
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/longest-valid-parentheses
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。#


def longestValidParentheses(s):
    if not s or len(s) <= 1:
        return 0

    res = 0
    left = right = 0
    for i in range(len(s)):
        if s[i] == "(":
            left += 1
        else:
            right += 1
        if left == right:
            res = max(res, 2*left)
        elif right > left:
            left = right = 0

    left = right = 0
    for i in reversed(range(len(s))):
        if s[i] == ")":
            right += 1
        else:
            left += 1
        if left == right:
            res = max(res, 2 * left)
        elif left > right:
            left = right = 0

    return res


def longestValidParentheses1(s):
    if not s or len(s) == 1:
        return 0
    n = len(s)
    dp = [0] * n
    res = 0
    for i in range(1, n):
        if s[i] == ')':
            if s[i-1] == '(':
                dp[i] = dp[i-2] + 2
            else:
                if i - dp[i-1] - 1 >= 0:
                    if s[i - dp[i-1] - 1] == '(':
                        dp[i] = dp[i-1] + 2 + dp[i - dp[i-1] - 2]

            if dp[i] > res:
                res = dp[i]

    return res


if __name__ == "__main__":
    s = "()(())"
    print(longestValidParentheses(s))
    print(longestValidParentheses1(s))
