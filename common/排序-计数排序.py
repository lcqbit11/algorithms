#/usr/bin/env python
# -*- coding: utf-8 -*-


def counting_sort(numbers, k):
    """
    :param numbers: List[int]
    :return: List[int]
    """
    length = len(numbers)
    counting_list = [0] * (k + 1)
    for i in range(length):
        counting_list[numbers[i]] += 1
    for i in range(1, k + 1):
        counting_list[i] += counting_list[i - 1]
    result = [0] * length
    for number in numbers:
        result[counting_list[number] - 1] = number
        counting_list[number] -= 1
    return result


if __name__ == "__main__":
    nums = [1, 3, 6, 2, 7, 1, 0, 2, 2, 5]
    print(counting_sort(nums, 7))