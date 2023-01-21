#!/usr/bin/env python
# -*- coding: utf-8 -*-

##
# 数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。#


def generateParenthesis(n):
    res = []
    res.append([None])
    res.append(["()"])
    for i in range(2, n+1):
        l = []
        for j in range(i):
            p = res[j]
            q = res[i - 1 - j]
            for l1 in p:
                for l2 in q:
                    if l1 is None:
                        l1 = ""
                    if l2 is None:
                        l2 = ""
                    item = "(" + l1 + ")" + l2
                    l.append(item)
        res.append(l)

    return res[n]


n = 3
print(generateParenthesis(n))
