#/usr/bin/env python
# -*- coding: utf-8 -*-
from collections import deque


def word_break(s, word_dict):
    """
    给定一个非空字符串s，一个单词集合list，
    请判断能否做到，对字符串s以某种方式分割后，所得到的所有词均出现在单词集合list中。
    请注意：
    1.字典中的单词可以被重复使用多次；
    2.可以假设字典中不包含重复的单词。
    :param s: str
    :param word_dict: List[str]
    :return: bool
    """
    d = [0]
    length = len(s)
    len_dict = [j for j in set(map(len, word_dict))]
    visited = [0] * (length + 1)
    while d:
        start = d.pop(0)
        for i in len_dict:
            if s[start:start+i] in word_dict:
                if start+i == length:
                    return True
                if visited[start+i] == 0:
                    d.append(start+i)
                    visited[start+i] = 1
    return False


def word_break_v2(s, word_dict):
    """
    :param s: str
    :param word_dict: List[str]
    :return: bool
    """
    n = len(s)
    dp = [False] * (n+1)  # 截止到第i个字母是否满足题目的条件
    dp[0] = True
    for i in range(1, n+1):
        for k in range(i):
            if dp[k] and s[k:i] in word_dict:
                dp[i] = True
    return dp[n]


if __name__ == "__main__":
    s = "leetcode"
    wordDict = ["leet", "code"]
    print(word_break_v2(s, wordDict))