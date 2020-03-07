#!/usr/bin/env python
# -*- coding: utf-8 -*-


class StackContainMin(object):
    def __init__(self):
        """
        定义栈的数据结构，请在该类型中实现一个能够得到栈的最小元素的min函数，在该栈中，调用min、push、pop的时间复杂度都是O(1)。
        """
        self.norm_stack = []
        self.min_stack = []
        self.min_value = float("inf")

    def push(self, val):
        self.norm_stack.append(val)
        if val < self.min_value:
            self.min_stack.append(val)
            self.min_value = val
        else:
            self.min_stack.append(self.min_value)

    def pop(self):
        self.norm_stack.pop()
        self.min_stack.pop()
        if self.min_stack:
            self.min_value = self.min_stack[-1]
        else:
            self.min_stack = None


if __name__ == "__main__":
    stack_contain_min = StackContainMin()
    stack_contain_min.push(3)
    stack_contain_min.push(4)
    print(stack_contain_min.norm_stack)
    print(stack_contain_min.min_stack)
    print(stack_contain_min.min_value)

    stack_contain_min.push(2)
    stack_contain_min.push(1)
    print(stack_contain_min.norm_stack)
    print(stack_contain_min.min_stack)
    print(stack_contain_min.min_value)

    stack_contain_min.pop()
    print(stack_contain_min.norm_stack)
    print(stack_contain_min.min_stack)
    print(stack_contain_min.min_value)

    stack_contain_min.pop()
    print(stack_contain_min.norm_stack)
    print(stack_contain_min.min_stack)
    print(stack_contain_min.min_value)

    stack_contain_min.push(0)
    print(stack_contain_min.norm_stack)
    print(stack_contain_min.min_stack)
    print(stack_contain_min.min_value)

