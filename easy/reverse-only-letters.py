#!/usr/bin/env python
# -*- coding: utf-8 -*-


def reverse_only_letters(S):
    """
    给定一个字符串S，返回其'反向'字符串表示，其中，非字母字符位置保持不变，字母字符的位置互相反转
    :param S: str
    :return: str
    """
    def is_letter(s):
        if (ord(s) >= ord('a') and ord(s) <= ord('z')) or (ord(s) >= ord('A') and ord(s) <= ord('Z')):
            return True
        return False

    if not S:
        return S
    l = len(S)
    res = ""
    for i in reversed(range(l)):
        if is_letter(S[i]):
            res += S[i]
    for i in range(l):
        if not is_letter(S[i]):
            res = res[:i] + S[i] + res[i:]

    return res


if __name__ == "__main__":
    S = "a-bC-dEf-ghIj"
    print(reverse_only_letters(S))