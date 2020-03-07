#!/usr/bin/env python
# -*- coding: utf-8 -*-

def minimum_window_substring(s, t):
    """
    给定一个字符串S和字符串T，请在S中找到一个包含T中所有字符的最小窗口，并且时间复杂度为O(n),
    如果S中没有满足条件的窗口，则返回空字符串""
    如果存在满足条件的窗口，那么可以保证S中这样的窗口唯一存在
    注意：对于T中重复字符的重复次数，在S中的最小窗口内也要重复相应的次数
    :param S:
    :param T:
    :return:
    """
    ls = len(s)
    lt = len(t)
    m = {}
    left = 0
    cnt_sum = 0
    min_len = ls+1
    res = ""
    for i in range(lt):
        m.setdefault(t[i], 0)
        m[t[i]] += 1
    for i in range(ls):
        if s[i] in m:
            m[s[i]] -= 1
            if m[s[i]] >= 0:
                cnt_sum += 1
        while cnt_sum == lt:
            if i - left + 1 < min_len:
                min_len = i - left + 1
                res = s[left:i+1]
            if s[left] in m:
                m[s[left]] += 1
                if m[s[left]] > 0:
                    cnt_sum -= 1
            left += 1
    return res

if __name__ == "__main__":
    S = "a"
    T = "a"
    print(minimum_window_substring(S, T))

