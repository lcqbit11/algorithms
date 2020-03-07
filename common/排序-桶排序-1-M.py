#/usr/bin/env python
# -*- coding: utf-8 -*-


def bucket_sort1m(numbers):
    """
    :param numbers: List[int]
    :return: List[int]
    """
    length = len(numbers)
    min_value = min(numbers)
    max_value = max(numbers)
    bucket_list = [0] * (max_value - min_value + 1)
    for i in range(length):
        bucket_list[numbers[i] - min_value] += 1
    result = []
    for k in range(len(bucket_list)):
        bucket_cap = bucket_list[k]
        while bucket_cap > 0:
            result.append(min_value + k)
            bucket_cap -= 1

    return result


if __name__ == "__main__":
    nums = [1, 3, 6, 2, 7, 1, 2, 2, 5]
    print(bucket_sort1m(nums))