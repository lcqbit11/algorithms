#!/usr/bin/env pyhton
# -*- coding: utf-8 -*-


def longest_palindromic_subsequence(s):  # 会超时
    '''
    param s: str
    return: str
    给定一个字符串s，请找出该字符串中最长的回文字符串。
    注意序列可以是不连续的，而子字符串是连续的。
    例如，
    Input: "bbbab"
    Output: 4
    One possible longest palindromic subsequence is "bbbb".
    Input: "cbbd"
    Output: 2
    One possible longest palindromic subsequence is "bb".
    '''
    def dp(i, j):
        if i == j:
            return 1
        elif i > j:
            return 0
        if s[i] == s[j]:
            return 2 + dp(i + 1, j - 1)
        else:
            return max(dp(i + 1, j), dp(i, j - 1))
            
    return dp(0, len(s) - 1)


def longest_palindromic_subsequence1(s):  # 会超时
    l = len(s)
    dp = [[0]*l for _ in range(l)]
    # for i in reversed(range(l)):
    for i in range(l-1, -1, -1):
        dp[i][i] = 1
        for j in range(i+1, l):
            if s[i] == s[j]:
                dp[i][j] = dp[i+1][j-1] + 2
            else:
                dp[i][j] = max(dp[i+1][j], dp[i][j-1])
    return dp[0][l-1]


def longest_palindromic_subsequence2(s):
    res = ''
    max_l = 0
    index = 0
    ll = len(s)
    for i in range(ll):
        # odd
        j = 0
        while i-j >= 0 and i+j < ll:
            if s[i-j] == s[i+j]:
                if max_l < 2*j+1:
                    max_l = 2*j+1
                    index = i
                    res = s[(i-j):(i+j+1)]
                j += 1
            else:
                break
        # even
        j = 0
        while i-j >= 0 and i+1+j < ll:
            if s[i-j] == s[i+1+j]:
                if max_l < 2*(j+1):
                    max_l = 2*(j+1)
                    index = i
                    res = s[(i-j):(i+1+j+1)]
                j += 1
            else:
                break
    return res


if __name__ == "__main__":
    s = "bbbab"
    print(longest_palindromic_subsequence2(s))
