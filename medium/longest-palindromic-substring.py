#!/usr/bin/env python
# -*- coding: utf-8 -*-


def longest_palindromic_subsequence(s):
    '''
    param s: str
    return: str
    给定一个字符串s，请找出该字符串中的最长回文字符串。
    注意：回文字符串在原始字符串中一定是连续的
    例如，
    Input: s = "babad"
    Output: "bab"
    Note: "aba" is also a valid answer.
    Input: s = "cbbd"
    Output: "bb"
    '''
    res = ''
    max_l = 0
    ll = len(s)
    for i in range(ll):
        # odd，回文字符串长度为奇数
        j = 0
        while i - j >= 0 and i + j < ll:
            if s[i - j] == s[i + j]:
                if max_l < 2 * j + 1:
                    max_l = 2 * j + 1
                    res = s[(i - j):(i + j + 1)]
                j += 1
            else:
                break
        # even，回文字符串长度为偶数
        j = 0
        while i - j >= 0 and i + 1 + j < ll:
            if s[i - j] == s[i + 1 + j]:
                if max_l < 2 * (j + 1):
                    max_l = 2 * (j + 1)
                    res = s[(i - j):(i + 1 + j + 1)]
                j += 1
            else:
                break
    return res


if __name__ == "__main__":
    s = "bbbab"
    print(longest_palindromic_subsequence(s))
