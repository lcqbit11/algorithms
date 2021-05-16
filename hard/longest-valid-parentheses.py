#!/usr/bin/env python
# -*- coding: utf-8 -*-


def longest_valid_parentheses(s):
    """
    给定一个只包含'('和')'的字符串，查找出有效括号字符串的最大连续长度
    :param s: str
    :return: int
    """
    res = 0
    s = ')' + s
    # dp的每一个位置上的值表示截止到当前位置，有效括号的最大长度，
    # 但是如果dp的当前位置不属于有效括号的范围内，则对应的dp位置上的值等于0
    dp = [0] * len(s)
    for i in range(1, len(s)):
        if s[i] == ')':
            if s[i - 1 - dp[i - 1]] == '(':  # '())((()))('
                dp[i] = dp[i - 1] + 2
            dp[i] += dp[i - dp[i]]
        res = max(res, dp[i])
    return res


def longest_valid_parentheses1(s):
    stack = [-1]
    res = 0
    for i in range(len(s)):  # '())((()))('
        if s[i] == '(':
            stack.append(i)
        else:
            stack.pop()
            if not stack:
                stack.append(i)
            else:
                res = max(res, i - stack[-1])
    return


def longest_valid_parentheses2(s):
    res = 0
    left = right = 0
    for i in range(len(s)):
        if s[i] == '(':
            left += 1
        else:
            right += 1
        if left == right:
            res = max(res, 2 * right)
        elif right > left:
            left = right = 0

    left = right = 0
    # for i in reversed(range(len(s))):
    for i in range(len(s)-1, -1, -1):
        if s[i] == '(':
            left += 1
        else:
            right += 1
        if left == right:
            res = max(res, 2 * left)
        elif left > right:
            left = right = 0

    return res


if __name__ == "__main__":
    s = '())((()))('
    s1 = '(()'
    # print(longest_valid_parentheses2(s1))
    print(longest_valid_parentheses(s))
