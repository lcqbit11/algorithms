#!/usr/bin/env python
# -*- coding: utf-8 -*-


def lcs(text1, text2):
    """
    给定两个字符串s1,s2，请返回两个字符串的最长公共子序列的长度。
    注意：s1子序列是指从s1中抽取出来的不改变其在s1中的相对位置的子字符串，
    我们不要求子字符串在s1中是连续的，s2子序列同理，
    两个字符串的公共子序列是指在s1和s2中都存在的子序列。
    :param s1: str
    :param s2: str
    :return: int
    """
    l1, l2 = len(text1) + 1, len(text2) + 1
    c = [[0] * l2 for _ in range(l1)]
    for i in range(l1):
        for j in range(l2):
            if i == 0 or j == 0:
                c[i][j] = 0
            elif text1[i - 1] == text2[j - 1]:
                c[i][j] = c[i - 1][j - 1] + 1
            else:
                c[i][j] = max(c[i - 1][j], c[i][j - 1])

    return c[l1 - 1][l2 - 1]


if __name__ == "__main__":
    s1 = "abcde"
    s2 = "ace"
    print(lcs(s1, s2))