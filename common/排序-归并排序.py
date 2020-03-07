#!/usr/bin/env python
# -*- coding: utf-8 -*-


def merge_sort(numbers):
    """
    :param numbers: List[int]
    :return: List[int]
    """
    def merge(number1, number2):
        len1 = len(number1)
        len2 = len(number2)
        res = []
        i = j = 0
        while i < len1 and j < len2:
            if number1[i] < number2[j]:
                res.append(number1[i])
                i += 1
            else:
                res.append(number2[j])
                j += 1
        if i == len1:
            res.extend(number2[j:])
        if j == len2:
            res.extend(number1[i:])
        return res

    if not numbers or len(numbers) <= 1:
        return numbers

    middle = int(len(numbers) / 2)
    left_list = merge_sort(numbers[:middle])
    right_list = merge_sort(numbers[middle:])
    return merge(left_list, right_list)


if __name__ == "__main__":
    nums = [9, 3, 6, 2, 7, 1, 2]
    print(merge_sort(nums))