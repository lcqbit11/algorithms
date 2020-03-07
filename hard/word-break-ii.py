#!/usr/bin/env python
# -*- coding: utf-8 -*-

def word_break_ii(s, word_dict):
    """
    对于一个非空的字符串s和一个单词字典，使用空格将字符串s分割成一句话，并且其中的每个单词都属于单词字典，
    函数最终返回所有可能的的字符串分割方式
    思路：参考word break中的只需要判断是哦负可以分割，这里需要返回所有的可能的分割的方式，
    所以需要word break中的dp的方法，并且要在此基础上加入dfs的方法。
    :param s: str
    :param word_dict: dict
    :return:
    """
    def dp(s_dp, word_dict_dp):
        ls = len(s_dp)
        dp_arr = [False] * (ls + 1)
        dp_arr[0] = True
        for i in range(1, ls+1):
            for k in range(i):
                if dp_arr[k] and s_dp[k:i] in word_dict_dp:
                    dp_arr[i] = True
        return dp_arr[-1]

    def dfs(s_dfs, word_dict_dfs, word_list):
        if dp(s_dfs, word_dict_dfs):
            if len(s_dfs) == 0:
                res.append(word_list[1:])
            for i in range(1, len(s_dfs)+1):
                if s_dfs[:i] in word_dict_dfs:
                    dfs(s_dfs[i:], word_dict_dfs, word_list + ' ' + s_dfs[:i])

    res = []
    dfs(s, word_dict, '')
    return res

if __name__ == '__main__':
    s = "catsanddog"
    wordDict = ["cat", "cats", "and", "sand", "dog"]
    print(word_break_ii(s, wordDict))