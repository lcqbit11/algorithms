#!/usr/bin/env python
# -*- coding:utf-8 -*-

def append_tail(stack1, stack2):
    """
    :param stack1: stack
    :param stack2: stack
    :return: void
    """
    if not stack2:
        while stack1:
            temp = stack1.pop()
            stack2.append(temp)

def delete_tail(stack1, stack2):
    """
    :param stack1: stack
    :param stack2: stack
    :return: void
    """
    while stack2:
        print(stack2[-1])
        del stack2[-1]

if __name__ == "__main__":
    stack1 = [1, 2, 3]
    stack2 = []
    append_tail(stack1, stack2)
    delete_tail(stack1, stack2)