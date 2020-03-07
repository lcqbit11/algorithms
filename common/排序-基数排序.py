#/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np

def radix_sort(numbers):
    """
    :param numbers: List[int]
    :return: List[int]
    """
    length = len(numbers)
    for i in range(2):
        counting_list = [[] for i in range(10)]
        for j in range(length):
            counting_list[int(numbers[j] / (10**i)) % 10].append(numbers[j])
        numbers = [j for i in counting_list for j in i]

    return numbers

if __name__ == "__main__":
    nums = [np.random.randint(100) for i in range(100)]
    print(nums)
    print(radix_sort(nums))