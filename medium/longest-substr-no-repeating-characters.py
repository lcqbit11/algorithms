#!/usr/bin/env python
# -*- coding: utf-8 -*-


def longest_substring_without_repeating_characters(s):
    """
    给定一个字符串，请返回不包含重复字符的子字符串的最大长度。
    :param s: str
    :return: int
    """
    d = {}
    start = 0  # start表示以当前字符为结尾且不包含重复字符的子字符串的开头位置
    res = 0
    for i, c in enumerate(s):
        if c in d:
            start = max(start, d[c] + 1)
        d[c] = i
        res = max(res, i - start + 1)

    return res


if __name__ == "__main__":
    # s = 'abba'
    # s = "abcabcbb"
    # s = 'pwwkew'
    s = input("请输入：")
    print(longest_substring_without_repeating_characters(s))