#!/usr/bin/env python
# -*- coding: utf-8 -*-


##
# 设计一个支持 push ，pop ，top 操作，并能在常数时间内检索到最小元素的栈。

# 实现 MinStack 类:

# MinStack() 初始化堆栈对象。
# void push(int val) 将元素val推入堆栈。
# void pop() 删除堆栈顶部的元素。
# int top() 获取堆栈顶部的元素。
# int getMin() 获取堆栈中的最小元素。

# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/min-stack
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。#


class MinStack:

    def __init__(self):
        self.stack = []


    def push(self, val):
        if not self.stack:
            self.stack.append((val, val))
        else:
            self.stack.append((val, min(val, self.stack[-1][1])))


    def pop(self):
        self.stack.pop()


    def top(self):
        return self.stack[-1][0]


    def getMin(self):
        return self.stack[-1][1]

