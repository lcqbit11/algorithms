#!/usr/bin/env python
# -*- coding: utf-8 -*-

def regular_expression_matching(s, p):
    """
    给定字符串s和模式p，实现支持'*'、'.'的正则表达式匹配，其中
    '.'可以表示任意字符
    '*'可以表示重复0次或者多次前面的字符
    s表示a-z之间的任意字符，p表示a-z之间任意字符、'*'、'.'
    :param s: str
    :param p: str
    :return: bool
    """
    # 如果s为空的话，则结果不一定直接跟p是否为空有关系，
    # 例如如果p='a*'，p可能匹配的内容是 *重复字符a 0次，那么匹配结果为空，此时p匹配s，返回True；
    # 如果 p='a'，那么此时p一定无法一个空的s，返回False。
    # 但是如果p为空的话，则最终返回结果只跟s是否为空有关
    if not p:
        return not s
    first_match = True if (s and s[0] == p[0]) or (s and p[0] == ".") else False
    if len(p) >= 2 and p[1] == "*":
        return (first_match and regular_expression_matching(s[1:], p)) or regular_expression_matching(s, p[2:])
    else:
        return first_match and regular_expression_matching(s[1:], p[1:])

if __name__ == "__main__":
    s = "aab"
    p = "c*a*b"
    print(regular_expression_matching(s, p))