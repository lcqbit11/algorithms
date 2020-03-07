#!/usr/bin/env python
# -*- coding: utf-8 -*-


def mergeSortedArray(num1, num2):
    """
    给定两个有序数组，将数组2合并到数组1上成为一个有序数组（假设数组1已经有了足够的空间来放得下数组1）
    :param num1: List[int]
    :param num2: List[int]
    :return mergedNum: List[int]
    """
    m = len(num1)
    n = len(num2)
    num1.extend([0] * n)
    sumLen = m + n
    i = m - 1
    j = n - 1
    for k in range(0, sumLen):
        if i < 0 and j < 0:
            break
        elif i >= 0 and j >= 0:
            if num1[i] < num2[j]:
                num1[sumLen - 1 - k] = num2[j]
                j -= 1
            else:
                num1[sumLen - 1 - k] = num1[i]
                i -= 1
        else:
            if i < 0:
                num1[sumLen - 1 - k] = num2[j]
                j -= 1
            else:
                num1[sumLen - 1 - k] = num1[i]
                i -= 1

    return num1


if __name__ == "__main__":
    num1 = [1, 2, 3, 4]
    num2 = [2, 3, 6, 8, 9]
    print(mergeSortedArray(num1, num2))