#!/usr/bin/env python
# -*- coding: utf-8 -*-
from utils.trieNode import TrieNode


class Trie(object):
    """
    实现一个trie树，包含插入、查找、开始字符判断的功能。
    """
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """
        :param word: word to be inserted to trie tree
        :return: void
        """
        p = self.root
        for c in word:
            diff_val = ord(c) - ord("a")
            if p.children[diff_val]:
                p = p.children[diff_val]
            else:
                child_trie_tree = TrieNode()
                p.children[diff_val] = child_trie_tree
                p = p.children[diff_val]
        p.isWord = True
        p.word = word

    def helper(self, word):
        p = self.root
        for c in word:
            diff_val = ord(c) - ord("a")
            if p.children[diff_val]:
                p = p.children[diff_val]
            else:
                return None
        return p

    def search(self, word):
        """
        Returns True if word is in the trie tree
        :param word: str
        :return: bool
        """
        p = self.helper(word)
        if p and p.isWord:
            return True
        return False

    def start_with(self, prefix):
        """
        Returns True if prefix matches the trie's start str
        :param prefix: str
        :return: bool
        """
        if self.helper(prefix):
            return True
        return False


class Trie1(object):
    def __init__(self):
        self.trie = {}

    def insert(self, word):
        t = self.trie
        for c in word:
            if c not in t:
                t[c] = {}
            t = t[c]
        t['-'] = True

    def search(self, word):
        t = self.trie
        for c in word:
            if c not in t:
                return False
            t = t[c]
        return '-' in t

    def start_with(self, prefix):
        t = self.trie
        for c in prefix:
            if c not in t:
                return False
            t = t[c]
        return True


if __name__ == "__main__":
    trie = Trie1()
    print(trie.insert("apple"))
    print(trie.search("apple"))
    print(trie.search("app"))
    print(trie.start_with("app"))
    print(trie.insert("app"))
    print(trie.search("app"))

