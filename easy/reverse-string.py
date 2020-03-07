#!/usr/bin/env python
# -*- coding: utf-8 -*-


def reverseString(s):
    """
    给定一个字符数组，请翻转这个字符数组。
    :type s: List[str]
    :rtype: None Do not return anything, modify s in-place instead.
    """
    if not s or len(s) == 1:
        return s
    l = len(s)
    for i in range(l//2):
        tmp = s[i]
        s[i] = s[l - 1 - i]
        s[l - 1 - i] = tmp
    return s


if __name__ == "__main__":
    s = ["h", "e", "l", "l", "o"]
    print(reverseString(s))