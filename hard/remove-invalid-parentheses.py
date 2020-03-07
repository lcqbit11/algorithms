#!/usr/bin/env python
# -*- coding: utf-8 -*-

class r_invalid_parentheses(object):
    def remove_invalid_parentheses(self, s):
        """
        将字符串中不符合条件的字符去除，以使得保留的字符串是有效的
        :param s: str
        :return: List[str]
        """
        # def is_valid(s):
        #     count = 0
        #     for char in s:
        #         if char == '(':
        #             count += 1
        #         if char == ')':
        #             count -= 1
        #         if count < 0:
        #             return False  # ())))
        #     return count == 0
        #
        # def dfs(s, start, l, r):
        #     if l == 0 and r == 0:
        #         if is_valid(s):
        #             self.ans.append(s)
        #         return
        #     for i in range(start, len(s)):
        #         if i - 1 >= start and s[i] == s[i - 1]:
        #             continue
        #         if r > 0 and s[i] == ')':
        #             dfs(s[:i] + s[i + 1:], i, l, r - 1)
        #         if l > 0 and s[i] == '(':
        #             dfs(s[:i] + s[i + 1:], i, l - 1, r)
        #
        # l = 0
        # r = 0
        # for char in s:
        #     if char == '(':
        #         l += 1
        #     elif char == ')':
        #         if l == 0:
        #             r += 1
        #         else:
        #             l -= 1
        # self.ans = []
        # dfs(s, 0, l, r)
        # return self.ans

        def is_valid_parentheses(s):
            count = 0
            for char in s:
                if char == "(":
                    count += 1
                if char == ")":
                    count -= 1
                if count < 0:
                    return False
            return count == 0

        def dfs(s, start, l, r):
            if l == 0 and r == 0:
                if is_valid_parentheses(s):
                    res.append(s)
                return []
            for i in range(start, len(s)):
                if i-1 >= start and s[i] == s[i - 1]:
                    continue
                if r > 0 and s[i] == ')':
                    dfs(s[:i] + s[i+1:], i, l, r-1)
                if l > 0 and s[i] == '(':
                    dfs(s[:i] + s[i+1:], i, l-1, r)
        l = 0
        r = 0
        for char in s:
            if char == '(':
                l += 1
            elif char == ')':
                if l == 0:
                    r += 1
                else:
                    l -= 1
        res = []
        dfs(s, 0, l, r)
        return res

if __name__ == "__main__":
    tmp = r_invalid_parentheses()
    s =  ")d))"
    print(tmp.remove_invalid_parentheses(s))