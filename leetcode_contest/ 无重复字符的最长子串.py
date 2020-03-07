#!/usr/bin/env python
# -*- coding: utf-8 -*-


def no_repeat_char(s):
    d = {}
    res = 0
    start = 0
    for i in range(len(s)):  # i 表示以第i个元素为结尾的子字符串
        if s[i] in d:
            start = max(start, d[s[i]] + 1)
        d[s[i]] = i
        res = max(res, i - start + 1)
    
    return res


if __name__ == "__main__":
    s = "abcabcbb"
    print(no_repeat_char(s))
        

