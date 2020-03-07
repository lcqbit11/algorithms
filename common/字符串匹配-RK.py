#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
RK 算法是借助于hash算法计算得到的
"""
def rk_match(s, part_s):
    """
    :param s: str
    :param part_s: str
    :return: match_index, -1 represents no match
    """
    def is_match(s1, s2):
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                return False
        return True

    l_s = len(s)
    l_part_s = len(part_s)
    hash_part_s = ord(part_s[0]) - ord('a')
    hash_s = ord(s[0]) - ord('a')
    d = 26
    k = 144451
    h = 1
    for i in range(1, l_part_s):
        hash_part_s  = (d * hash_part_s + ord(part_s[i]) - ord('a')) % k
        hash_s = (d * hash_s + ord(s[i]) - ord('a')) % k
        h = (h * d) % k

    for j in range(l_s - l_part_s + 1):
        if hash_part_s == hash_s and is_match(s[j:j+l_part_s], part_s):
            return j
        hash_s = (d * (hash_s - h * (ord(s[j]) - ord('a'))) + ord(s[j + l_part_s]) - ord('a')) % k

    return -1

if __name__ == "__main__":
    s = "abcdefgdcbaefg"
    part_s = "def"
    print(rk_match(s, part_s))