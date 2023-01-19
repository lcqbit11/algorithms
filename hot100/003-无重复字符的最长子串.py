#!/usr/bin/env python
# -*- coding: utf-8 -*-

##
# 给定一个字符串 s ，请你找出其中不含有重复字符的 最长子串 的长度。#


def lengthOfLongestSubstring(s):
    if not s:
        return 0
    res = 0
    d = dict()
    start = 0
    for i, v in enumerate(s):
        if v in d:
            start = max(start, d[v] + 1)
        d[v] = i
        res = max(res, i - start + 1)

    return res


if __name__ == "__main__":
    s = "abcabcbb"
    print(lengthOfLongestSubstring(s))
