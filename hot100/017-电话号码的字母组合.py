#!/usr/bin/env python
# -*- coding: utf-8 -*-

##
# 给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。答案可以按 任意顺序 返回。
#
# 给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/letter-combinations-of-a-phone-number
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。#


def letterCombinations(digits):
    if not digits:
        return []

    phoneMap = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz",
    }

    def loop(index):
        if index == len(digits):
            combinations.append("".join(combination))
        else:
            digit = digits[index]
            for char in phoneMap[digit]:
                combination.append(char)
                loop(index + 1)
                combination.pop()

    combination = []
    combinations = []
    loop(0)

    return combinations


digits = "23"
print(letterCombinations(digits))
