#!/usr/bin/env python
# -*- coding: utf -*-


class TrieNode(object):
    def __init__(self):
        self.children = [None] * 26  # 该TrieNode的孩子
        self.isWord = False  # 该TrieNode是否是完整的单词
        self.word = ""  # 该TrieNode所表示的单词