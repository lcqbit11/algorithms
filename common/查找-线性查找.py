#/usr/bin/env python
# -*- coding: utf-8 -*-


def linear_search(numbers, n, k):
    """
    :param numbers: List[int]
    :param n: int
    :param k: int
    :return: int
    """
    for i in range(0, n):
        if numbers[i] == k:
            return i
    return -1


if __name__ == "__main__":
    nums = [1, 3, 6, 2, 7, 1, 2, 2, 5]
    print(linear_search(nums, len(nums), 7))