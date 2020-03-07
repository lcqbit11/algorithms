#!/usr/bin/env python
# -*- coding: utf-8 -*-

def top_n(numbers, n):
    """
    :param numbers: List[int]
    :return: List[int]
    """
    def heap(nums, low, high):
        i = low
        k = 2 * low + 1
        while k <= high:
            if k + 1 <= high and nums[k] > nums[k + 1]:
                k = k + 1
            if nums[i] > nums[k]:
                nums[i], nums[k] = nums[k], nums[i]
            i = k
            k = 2 * k + 1

    result = numbers[:n]
    middle = int((n-2)/2) if n >= 2 else 0
    for i in range(middle + 1):
        heap(result, middle-i, n-1)

    for j in range(n, len(numbers)):
        if result[0] < numbers[j]:
            result[0] = numbers[j]
            heap(result, 0, n-1)

    return result

if __name__ == "__main__":
    nums = [68, 65, 71, 75, 93, 56, 44, 29, 20, 18, 30, 34]
    n = 5
    print(top_n(nums, n))