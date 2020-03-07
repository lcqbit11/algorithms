#!/usr/bin/env python
# -*- coding: utf-8 -*-


def water_and_jug_problem(x, y, z):
    """
    给定两个容量为x升和y升的水桶，有无限量的水供应，请计算是否能够使用两个水桶精确量出z升水。
    请注意：如果z升水是可以精确量出来的，那么最终这z升水一定是装在其中一个桶或者同时装在两个桶中的。
    :param x: int
    :param y: int
    :param z: int
    :return: bool
    """
    if z > x + y:
        return False
    if z == 0 or x == z or y == z or x + y == z:
        return True
    if min(x, y) == 0:
        return True if max(x, y) == z else False
    n = min(x, y)
    while n > 1:
        if x % n == 0 and y % n == 0:
            break
        n -= 1
    if z % n == 0:
        return True
    return False


def water_and_jug_problem1(x, y, z):
    """
    问题解法：
    这道问题其实可以转换为有一个很大的容器，我们有两个杯子，容量分别为x和y，问我们通过用两个杯子往里倒水，
    和往出舀水，问能不能使容器中的水刚好为z升。那么我们可以用一个公式来表达：
    z = m * x + n * y
    其中m，n为舀水和倒水的次数，正数表示往里舀水，负数表示往外倒水，那么题目中的例子可以写成: 4 = (-2) * 3 + 2 * 5，
    即3升的水罐往外倒了两次水，5升水罐往里舀了两次水。那么问题就变成了对于任意给定的x,y,z，存不存在m和n使得上面的等式成立。
    根据裴蜀定理，ax + by = d的解为 d = gcd(x, y)，那么我们只要z % d == 0，上面的等式就有解，所以问题就迎刃而解了，
    我们只要看z是不是x和y的最大公约数的倍数就行了，别忘了还有个限制条件x + y >= z，因为x和y不可能称出比它们之和还多的水。
    """
    def gcd(x, y):
        return x if y == 0 else gcd(y, x % y)
    x, y = max(x, y), min(x, y)
    return z == 0 or (x + y >= z and z % gcd(x, y) == 0)


if __name__ == "__main__":
    x, y, z = 3, 5, 4
    print(water_and_jug_problem1(x, y, z))