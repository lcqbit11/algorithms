#! /usr/bin/python env
# -*- coding: utf-8 -*-


def isValid(s):
    """
    字符串里面只包含'(', ')', '{', '}', '[', ']'这6个字符，判断该字符是否是合理的
    :param s:
    :return bool:
    """
    stack = []
    res = ["()", "[]", "{}"]
    for i in range(0, len(s)):
        stack.append(s[i])
        if len(stack) >= 2 and stack[-2] + stack[-1] in res:
            stack.pop()
            stack.pop()

    return len(stack) == 0


def is_valid1(s):
    res = []
    for i in range(len(s)):
        res.append(s[i])
        if len(res) >= 2:
            if res[-2] + res[-1] == '()':
                res.pop()
                res.pop()
    return not res


def is_valid2(s):
    cnt = 0
    for i in range(len(s)):
        if s[i] == '(':
            cnt += 1
        else:
            if cnt == 0:
                return False
            else:
                cnt -= 1
    return cnt == 0


if __name__ == "__main__":
    print(isValid("()[]{}"))
    print(isValid("([]{})"))
    print(isValid("([]{()})"))
    print(isValid("(((())))){}"))
    print('\n')
    print(is_valid1("()"))
    print(is_valid1("())"))
    print(is_valid1("(((())))"))
    print('\n')
    print(is_valid2("()"))
    print(is_valid2("())"))
    print(is_valid2("(((())))"))