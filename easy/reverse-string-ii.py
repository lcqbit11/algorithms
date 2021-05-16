#!/usr/bin/env python
# -*- coding: utf-8 -*-


def reverse_string(s, k):
    """
    给定一个字符串s，正整数k，对于每2*k个字符，请翻转前k个字符。
    如果剩余的字符长度小于k，请把他们全部翻转即可；
    如果剩余的字符长度小于2*k但是大于等于k，请翻转前k个字符并保持剩下的字符不变。
    :type s: str
    :type k: int
    :rtype: str
    """
    if not s or len(s) <= 1 or k <= 1:
        return s

    def reverse_k(s, start, end):
        s1 = s[:start]
        s2 = ''
        s3 = s[min(end+1, len(s)):]
        for i in range(end, start-1, -1):
            s2 += s[i]
        return s1+s2+s3

    ll = len(s)
    end = start = 0
    while start < ll:
        end = start + 2*k - 1
        reverse_end = min(start+k-1, ll-1)
        s = reverse_k(s, start, reverse_end)
        start = end + 1
    return s


if __name__ == '__main__':
    s = "abcdefghijkmln"
    k = 3
    print(s)
    print(reverse_string(s, k))