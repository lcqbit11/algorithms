#!/usr/bin/env python
# -*- coding: utf-8 -*-

def wildcard_matching(s, p):
    """
    给定字符串s和模式p，请实现支持'?'和'*'的通配符匹配
    '?'可以匹配任意单个字母
    '*'可以匹配任意字母序列（包括空的字符序列）
    s 可以为空，包含a-z之间的任意字母
    p 可以为空，包含a-z之间的任意字母、或者字符'?'和'*'
    :param s:
    :param p:
    :return:
    """
    i = j = 0
    iStar = 0
    jStar = -1
    while i < len(s):
        if j < len(p) and (s[i] == p[j] or p[j] == '?'):
            i += 1
            j += 1
        elif j < len(p) and p[j] == '*':
            iStar = i
            jStar = j
            j += 1
        elif jStar >= 0:
            iStar += 1
            i = iStar
            j = jStar + 1
        else:
            return False
    while j < len(p) and p[j] == '*':
        j += 1
    return j == len(p)

if __name__ == "__main__":
    s = "acdcb"
    p = "a*c?b"
    # s = "adceb"
    # p = "*a*b"
    print(wildcard_matching(s, p))