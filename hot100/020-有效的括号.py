#!/usr/bin/env python
# -*- coding: utf-8 -*-

##
# 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。
#
# 有效字符串需满足：
#
# 左括号必须用相同类型的右括号闭合。
# 左括号必须以正确的顺序闭合。
# 每个右括号都有一个对应的相同类型的左括号。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/valid-parentheses
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。#


def isValid(s):
    if not s:
        return False
    valid = ['()', '{}', '[]']
    res = []
    for item in s:
        res.append(item)
        if len(res) >= 2:
            if ''.join(res[len(res)-2:]) in valid:
                res.pop()
                res.pop()

    return len(res) == 0


s = "()[]{}["
print(isValid(s))

