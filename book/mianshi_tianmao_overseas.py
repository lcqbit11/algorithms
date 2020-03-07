#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
给定三个已知变量：
商品title的分词列表s，长度为30；
一个map格式的同义词词库，key表示单词，value表示该单词的相似单词list（或者是list或者是逗号分割的单词字符串）；
一个map格式的重要性分数词库，key表示单词，value表示该单词的重要性分数。

要求条件：
将该长度为30的title缩短至长度为10，通过下面两种方式进行缩短：
1.原始title中包含冗余的单词，例如“2020年”这种不重要的单词；
2.原始title中包含同义词单词。

执行代码：
基于上面的已知变量和要求条件，我们可以基于单词的重要性分数词库和同义词词库来去除冗余和同义词单词，最终只保留10个单词。
"""


def shorten_title(s, near_map, score_map):

    def if_removed(sorted_input_map1, word):
        if not sorted_input_map1 or len(sorted_input_map1) <= 10:
            return
        length = len(sorted_input_map1)
        for i in range(length):
            if sorted_input_map1[i][0] == word and i >= 10:
                del sorted_input_map1[i]
                return

    def input_score_mapping(s, score_map):
        if not s or not score_map:
            return
        ll = len(s)
        m = {}
        for i in range(ll):
            if ll[i] not in score_map:
                m[ll[i]] = -1
            else:
                m[ll[i]] = score_map[ll[i]] if not score_map[ll[i]] else -1
        
        return m  

    if not s:
        return 
    l = len(s)
    sorted_input_map = {}
    sorted_input_map = input_score_mapping(s, score_map)
    sorted_input_map1 = sorted(sorted_input_map.items(), key=lambda x: x[1], reverse=False)
    for i in range(s):
        if s[i] in near_map and not near_map[s[i]]:
            sim_words_list = sim_words.split(",")
            for word in sim_words_list:
                if_removed(sorted_input_map1, word)

    if len(sorted_input_map1) > 10:
        sorted_input_map1 = sorted_input_map1[:10]

    return [x[0] for x in sorted_input_map1]