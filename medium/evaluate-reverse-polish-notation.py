#!/usr/bin/env python
# -*- coding: utf-8 -*-


def evaluate_reverse_polish_notation(nums):
    """
    请使用逆波兰表达式计算算术表达式的值，+, -, *, /这四种均为有效的表达式，每个操作数可以是整数或者另一个表达式。
    请注意：
    1.两个整数之间的出发运算只需要截取保留整数部分；
    2.假设给定的逆波兰表达式总是有效的，因此是能够计算出来一个确定的结果的。
    :param nums: List[str]
    :return: int
    """
    stack = []
    tmp = 0
    for s in nums:
        if s in ["+", "-", "*", "/"]:
            b = stack.pop()
            a = stack.pop()
            if s == "+":
                tmp = a + b
            elif s == "-":
                tmp = a - b
            elif s == "*":
                tmp = a*b
            elif s == "/":
                tmp = int(float(a)/float(b))
            stack.append(tmp)
        else:
            stack.append(int(s))

    return stack.pop()


if __name__ == "__main__":
    # nums = ["4","13","5","/","+"]
    nums = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
    print(evaluate_reverse_polish_notation(nums))

