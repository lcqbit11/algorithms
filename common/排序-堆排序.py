#!/usr/bin/env python
# -*- coding: utf-8 -*-


def heap_sort(numbers):
    """
    :param numbers: List[int]
    :return: List[int]
    """
    def max_heap(nums, min_index, max_index):
        node = min_index
        k = 2 * node + 1
        while k <= max_index and node <= max_index:
            if k + 1 <= max_index and nums[k] < nums[k+1]:
                k = k + 1
            if nums[node] < nums[k]:
                nums[node], nums[k] = nums[k], nums[node]
                node = k
                k = 2 * node + 1
            else:
                break

    length = len(numbers)
    middle_node = int((length - 1) / 2)
    for i in range(middle_node):
        max_heap(numbers, middle_node - i, length - 1)

    for i in range(length - 1):
        numbers[0], numbers[length - 1 - i] = numbers[length - 1 - i], numbers[0]
        max_heap(numbers, 0, length-1-i-1)
    return numbers


if __name__ == "__main__":
    nums = [9, 3, 6, 2, 7, 1, 2]
    old = ""
    for number in nums:
        old += " "
        old += str(number)
    print(old)
    heap_sort(nums)
    new = ""
    for number in nums:
        new += " "
        new += str(number)
    print(new)






