#/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np


def bucket_sort01(numbers):
    """
    :param numbers: List[int]
    :return: List[int]
    """
    def bubble_sort(nums):
        l = len(nums)
        for i in range(0, l - 1):
            for j in range(0 ,l - i):
                if nums[i] > numbers[j]:
                    nums[i], nums[j] = nums[j], nums[i]

    length = len(numbers)
    bucket_list = [[] for i in range(length)]
    for k in range(length):
        bucket_list[int(numbers[k] * length)].append(numbers[k])
    for bucket in bucket_list:
        bubble_sort(bucket)

    return [i for j in bucket_list for i in j]


if __name__ == "__main__":
    nums = [round(np.random.random(), 2) for i in range(100)]
    print(nums)
    print(bucket_sort01(nums))