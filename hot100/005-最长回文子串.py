#!/usr/bin/env python
# -*- coding: utf-8 -*-

##
# 给你一个字符串 s，找到 s 中最长的回文子串。

# 如果字符串的反序与原始字符串相同，则该字符串称为回文字符串。#


def longestPalindrome(s):
    max_sub = 0
    index = 0
    l = len(s)
    for i in range(l):
        # odd
        for j in range(l):
            if i - j >= 0 and i + j < l:
                if s[i - j] == s[i + j]:
                    if max_sub < 2*j + 1:
                        max_sub = 2*j + 1
                        index = i
                else:
                    break
        # even
        for j in range(l):
            if i - j >= 0 and i + 1 + j < l:
                if s[i - j] == s[i + 1 + j]:
                    if max_sub < (j + 1) * 2:
                        max_sub = (j + 1) * 2
                        index = i
                else:
                    break
    return s[(index-(max_sub-1)//2):(index-(max_sub-1)//2+max_sub)]


def longestPalindrome_2(s):
    if not s or len(s) <= 1:
        return s
    
    res = ""
    max_len = 0
    index = 0
    l = len(s)
    for i in range(l):
        # odd
        for j in range(l):
            if i-j >= 0 and i+j < l:
                if s[i-j] == s[i+j]:
                    if max_len < 2*j+1:
                        max_len = 2*j+1
                        index = i
                else:
                    break
        if max_len > len(res):
            res = s[(index-(max_len-1)//2):(index+(max_len-1)//2+1)]

        # even
        for j in range(l):
            if i-j >= 0 and i+1+j < l:
                if s[i-j] == s[i+1+j]:
                    if max_len < 2*(j+1):
                        max_len = 2*(j+1)
                        index = i
                else:
                    break
        if max_len > len(res):
            res = s[(index-(max_len-2)//2):(index+1+(max_len-2)//2+1)]
    return res


def longestPalindrome_3(s):
    if not s or len(s) < 2 or s == s[::-1]:
        return s
    
    res = s[0]
    max_len = 1
    l = len(s)
    for i in range(1, l):
        odd = s[i-max_len-1 : i+1]
        even = s[i-max_len : i+1]
        if odd == odd[::-1] and i-max_len-1 >= 0:
            res = odd
            max_len = len(odd)
            continue
        if even == even[::-1] and i-max_len >= 0:
            res = even
            max_len = len(even)
            continue
    
    return res


s = "babad"
# s = "aacabdkacaa"
# print(longestPalindrome(s))
# print(longestPalindrome_2(s))
print(longestPalindrome_3(s))
