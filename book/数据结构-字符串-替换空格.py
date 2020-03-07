#!/usr/bin/env python
# -*- coding: utf-8 -*-

def replace_space(s):
    """
    :param s: str
    :return: str
    """
    s = list(s)
    space_num = 0
    l_s = len(s)
    for i in range(l_s):
        if s[i] == ' ':
            space_num += 1
            # s.join(" ")
    print(s)
    s += ['0'] * 2 * space_num
    print(s)
    end_index = len(s) - 1
    print(end_index)
    for j in reversed(range(0, l_s)):
        if s[j] == ' ':
            s[end_index-2:end_index+1] = ['%', '2', '0']
            end_index -= 3
        else:
            s[end_index] = s[j]
            end_index -= 1
    return "".join(s)

if __name__ == "__main__":
    s = "we are happy"
    print(replace_space(s))